from backend.graph.graph import graph

initial_state = {
    "company": "Tesla",
    "query": "Perform due diligence on Tesla",
    "news": "",
    "financials": "",
    "legal": "",
    "risk": "",
    "report": "",
    "selected_agents": []
}

result = graph.invoke({
    "company": "Microsoft",
    "pdf_path": "backend/data/documents/MSFT_FY25q4_10K.pdf",
    "query": "Perform complete due diligence",

    "news": "",
    "financials": "",
    "legal": "",
    "risk": "",
    "report": "",

    "selected_agents": []
})