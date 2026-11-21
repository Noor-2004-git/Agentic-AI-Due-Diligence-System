from backend.graph.state import GraphState
from backend.executor.registry import AGENT_REGISTRY


def execute_selected_agents(state: GraphState):

    selected = state["selected_agents"]

    for agent_name in selected:

        agent = AGENT_REGISTRY.get(agent_name)

        if agent:

            print(f"\n========== Running {agent_name.upper()} Agent ==========\n")

            state = agent(state)

    return state