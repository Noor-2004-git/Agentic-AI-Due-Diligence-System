from backend.graph.state import GraphState
from backend.services.llm_service import ask_llm


def report_agent(state: GraphState):

    print("\n========== REPORT GENERATOR ==========\n")

    company = state["company"]

    prompt = f"""
Generate a professional Due Diligence Report.

Company:
{company}

NEWS ANALYSIS:
{state.get("news", "Not Available")}

FINANCIAL ANALYSIS:
{state.get("financials", "Not Available")}

LEGAL ANALYSIS:
{state.get("legal", "Not Available")}

RISK ANALYSIS:
{state.get("risk", "Not Available")}

Create a report with:

1. Executive Summary

2. News Overview

3. Financial Analysis

4. Legal Risks

5. Overall Risk Assessment

6. Investment Recommendation
"""

    report = ask_llm(prompt)

    print("\n========== REPORT FROM LLM ==========\n")
    print(repr(report))

    state["report"] = report

    return state