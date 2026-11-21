from backend.graph.state import GraphState
from backend.tools.finance_tools import get_financial_data
from backend.services.llm_service import ask_llm
from backend.tools.ticker_tool import get_ticker

def finance_agent(state: GraphState):

    company = state["company"]

    ticker = get_ticker(company)

    print(f"Resolved ticker: {ticker}")

    financial_data = get_financial_data(ticker)

    prompt = f"""
You are a Senior Financial Due Diligence Consultant at Alvarez & Marsal.

Analyze the following company financial data.

Provide:

1. Financial Health
2. Profitability
3. Business Strength
4. Possible Financial Risks
5. Investment Outlook

Financial Data:

{financial_data}
"""

    analysis = ask_llm(prompt)

    state["financials"] = analysis

    print("\n===== Financial Analysis =====\n")
    print(analysis)

    return state