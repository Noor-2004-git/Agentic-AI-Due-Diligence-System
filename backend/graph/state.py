from typing import TypedDict, List

class GraphState(TypedDict):
    company: str
    pdf_path: str
    query: str

    news: str
    financials: str
    legal: str
    risk: str

    report: str

    selected_agents: List[str]