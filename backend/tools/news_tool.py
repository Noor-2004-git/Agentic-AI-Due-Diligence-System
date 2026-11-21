import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_news(company: str) -> str:
    """
    Search for the latest news about a company using Tavily.
    """

    response = client.search(
        query=f"Latest news about {company}",
        max_results=5
    )

    results = response.get("results", [])

    news = ""

    for article in results:
        news += f"Title: {article['title']}\n"
        news += f"Content: {article['content']}\n\n"

    return news