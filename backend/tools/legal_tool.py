from backend.tools.news_tool import client


def search_legal(company: str) -> str:

    response = client.search(
        query=f"""
        Latest lawsuits, legal issues,
        regulatory investigations,
        compliance violations involving {company}
        """,
        max_results=5
    )

    results = response.get("results", [])

    legal_info = ""

    for article in results:
        legal_info += f"Title: {article['title']}\n"
        legal_info += f"Content: {article['content']}\n\n"

    return legal_info