from backend.agents.news_agent import news_agent
from backend.agents.finance_agent import finance_agent
from backend.agents.legal_agent import legal_agent
from backend.agents.risk_agent import risk_agent

AGENT_REGISTRY = {
    "news": news_agent,
    "finance": finance_agent,
    "legal": legal_agent,
    "risk": risk_agent
}