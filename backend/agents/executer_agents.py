from backend.graph.state import GraphState
from backend.executor.executor import execute_selected_agents


def executor_agent(state: GraphState):

    print("\n========== EXECUTOR ==========\n")

    state = execute_selected_agents(state)

    return state