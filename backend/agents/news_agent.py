from backend.graph.state import GraphState
from backend.tools.news_tool import search_news
from backend.services.llm_service import ask_llm


def news_agent(state: GraphState):

    company = state["company"]

    articles = search_news(company)

    prompt = f"""
You are a financial due diligence consultant.

Read the following latest news about {company}.

Summarize it into 5-6 bullet points.

Mention:
- Major announcements
- Financial/business impact
- Risks
- Opportunities

News:

{articles}
"""

    summary = ask_llm(prompt)

    state["news"] = summary

    print(summary)

    return state