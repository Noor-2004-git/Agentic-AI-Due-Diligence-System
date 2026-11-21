from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_risk(company: str):

    query = f"""
    {company} business risks,
    operational risks,
    cybersecurity,
    supply chain,
    regulatory risks,
    market risks
    """

    response = tavily_client.search(
        query=query,
        max_results=5
    )

    return response["results"]