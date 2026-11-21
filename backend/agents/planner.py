from backend.graph.state import GraphState
from backend.services.llm_service import ask_llm


def planner(state: GraphState):

    company = state["company"]
    query = state["query"]

    prompt = f"""
You are the Planner Agent of an AI Due Diligence System.

Your job is to decide which specialist agents should execute.

Available agents:
- News
- Finance
- Legal
- Risk

User Request:
{query}

Company:
{company}

Rules:
- Return ONLY the required agent names.
- One agent name per line.
- Do not explain your answer.
- Only choose from: News, Finance, Legal, Risk.
"""

    response = ask_llm(prompt)

    print("\n===== Planner Decision =====\n")
    print(response)

    selected_agents = []

    for line in response.splitlines():

        agent = line.strip().lower()

        if agent in ["news", "finance", "legal", "risk"] and agent not in selected_agents:
            selected_agents.append(agent)

    state["selected_agents"] = selected_agents

    return state