from backend.graph.state import GraphState
from backend.tools.risk_tool import search_risk
from backend.services.llm_service import ask_llm


def risk_agent(state: GraphState):

    print("\n========== Running RISK Agent ==========\n")

    company = state["company"]

    risk_info = search_risk(company)

    prompt = f"""
You are a Senior Due Diligence Risk Consultant.

Analyze the following information.

Company:
{company}

Risk Information:
{risk_info}

Provide:

1. Financial Risks

2. Operational Risks

3. Regulatory Risks

4. Market Risks

5. Cybersecurity Risks

6. Overall Risk Rating (Low/Medium/High)

7. Recommendation
"""

    analysis = ask_llm(prompt)

    print("\n===== Risk Analysis =====\n")
    print(analysis)

    state["risk"] = analysis

    return state