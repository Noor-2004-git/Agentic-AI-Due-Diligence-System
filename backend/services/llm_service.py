import os
import re
import time

import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# llama-3.3-70b-versatile was shut down on Groq (free/dev tier) on 16 Aug 2026
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

MAX_RETRIES = 6
# Free tier is ~8000 tokens/min, so keep each prompt well under that.
MAX_PROMPT_CHARS = 12000  # roughly 3k tokens
MAX_OUTPUT_TOKENS = 2000


def _wait_time(error, attempt):
    """Use the server's 'try again in Xs' hint when present, else back off."""
    match = re.search(r"try again in ([\d.]+)s", str(error))
    if match:
        return float(match.group(1)) + 1
    return min(2 ** attempt * 5, 60)


def ask_llm(prompt):

    if len(prompt) > MAX_PROMPT_CHARS:
        prompt = prompt[:MAX_PROMPT_CHARS] + "\n\n[...input truncated...]"

    kwargs = {}
    if "gpt-oss" in MODEL:
        # Reasoning tokens count toward the per-minute limit
        kwargs["reasoning_effort"] = "low"

    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=MAX_OUTPUT_TOKENS,
                **kwargs,
            )
            return response.choices[0].message.content or ""

        except groq.RateLimitError as e:
            if attempt == MAX_RETRIES - 1:
                raise
            wait = _wait_time(e, attempt)
            print(f"Rate limited, waiting {wait:.0f}s (attempt {attempt + 1}/{MAX_RETRIES})")
            time.sleep(wait)