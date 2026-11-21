from langgraph.graph import StateGraph, START, END

from backend.graph.state import GraphState
from backend.agents.report_agent import report_agent
from backend.agents.planner import planner
from backend.agents.executer_agents import executor_agent

builder = StateGraph(GraphState)

def planner_node(state):
    print(">>> ENTERED PLANNER NODE")
    return planner(state)

def executor_node(state):
    print(">>> ENTERED EXECUTOR NODE")
    return executor_agent(state)

def report_node(state):
    print(">>> ENTERED REPORT NODE")
    return report_agent(state)

builder.add_node("planner", planner_node)
builder.add_node("executor", executor_node)
builder.add_node("report_generator", report_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", "report_generator")
builder.add_edge("report_generator", END)

graph = builder.compile()
# from langgraph.graph import StateGraph, START, END

# from backend.graph.state import GraphState
# from backend.agents.legal_agent import legal_agent
# from backend.agents.planner import planner
# from backend.agents.news_agent import news_agent
# from backend.agents.finance_agent import finance_agent


# builder = StateGraph(GraphState)


# # -----------------------
# # Nodes
# # -----------------------
# builder.add_node("planner", planner)
# builder.add_node("news_node", news_agent)
# builder.add_node("finance_node", finance_agent)

# builder.add_node("legal_node", legal_agent)
# # -----------------------
# # Router Functions
# # -----------------------



# def route_from_planner(state: GraphState):

#     agents = state["selected_agents"]

#     if "news" in agents:
#         return "news"

#     if "finance" in agents:
#         return "finance"

#     if "legal" in agents:
#         return "legal"

#     return END


# def route_after_news(state: GraphState):

#     agents = state["selected_agents"]

#     if "finance" in agents:
#         return "finance"

#     if "legal" in agents:
#         return "legal"

#     return END


# def route_after_finance(state: GraphState):

#     agents = state["selected_agents"]

#     if "legal" in agents:
#         return "legal"

#     return END
# # -----------------------
# # Graph
# # -----------------------

# builder.add_edge(START, "planner")

# builder.add_conditional_edges(
#     "planner",
#     route_from_planner,
#     {
#         "news": "news_node",
#         "finance": "finance_node",
#         "legal": "legal_node",
#         END: END,
#     },
# )

# builder.add_conditional_edges(
#     "news_node",
#     route_after_news,
#     {
#         "finance": "finance_node",
#         "legal": "legal_node",
#         END: END,
#     },
# )

# builder.add_conditional_edges(
#     "finance_node",
#     route_after_finance,
#     {
#         "legal": "legal_node",
#         END: END,
#     },
# )

# builder.add_edge("legal_node", END)

# graph = builder.compile()