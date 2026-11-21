from backend.graph.state import GraphState
from backend.tools.legal_tool import search_legal
from backend.services.llm_service import ask_llm
from backend.rag.retriever import retrieve_documents


def legal_agent(state: GraphState):

    print("\n========== Running LEGAL Agent ==========\n")

    company = state["company"]
    pdf_path = state["pdf_path"]

    retrieval_query = f"""
    {company} legal proceedings,
    litigation,
    compliance,
    regulatory issues
    """
    
    # Retrieve relevant sections from the uploaded annual report
    rag_docs = retrieve_documents(
        pdf_path,
        retrieval_query
    )

    rag_context = "\n\n".join(
        [doc.page_content for doc in rag_docs]
    )
    print("\n===== RAG CONTEXT =====\n")
    print(rag_context[:1500])
    # Latest legal information from the web
    legal_data = search_legal(company)

    prompt = f"""
You are a Senior Legal Due Diligence Consultant.

You have TWO information sources.

====================================================
SOURCE 1 : LATEST WEB INFORMATION
====================================================

{legal_data}

====================================================
SOURCE 2 : OFFICIAL COMPANY ANNUAL REPORT
====================================================

{rag_context}

====================================================
TASK
====================================================

Using BOTH the latest web information and the official annual report, prepare a professional legal due diligence report.

Include:

1. Current Legal Issues

2. Ongoing Litigation

3. Regulatory Investigations

4. Compliance Concerns

5. Legal Risks identified from the Annual Report

6. Recent Legal Developments identified from Web Search

7. Overall Legal Risk Rating
(Low / Medium / High)

8. Final Due Diligence Recommendation

If the two sources provide different information, mention both.
"""

    analysis = ask_llm(prompt)

    state["legal"] = analysis

    print("\n===== Legal Analysis =====\n")
    print(analysis)

    return state