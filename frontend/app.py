import os
import sys
import streamlit as st

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from backend.graph.graph import graph
st.set_page_config(
    page_title="AI Due Diligence Consultant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Due Diligence Consultant")
st.markdown("### Multi-Agent Due Diligence using LangGraph + RAG")

st.divider()

company = st.text_input(
    "Company Name",
    placeholder="Microsoft"
)

query = st.text_area(
    "Query",
    value="Perform complete due diligence on this company."
)

uploaded_file = st.file_uploader(
    "Upload Annual Report (PDF)",
    type=["pdf"]
)

analyze = st.button("🚀 Analyze Company", use_container_width=True)

if analyze:

    if company == "":
        st.error("Please enter a company name.")
        st.stop()

    if uploaded_file is None:
        st.error("Please upload the Annual Report PDF.")
        st.stop()

    os.makedirs("backend/data/documents", exist_ok=True)

    pdf_path = os.path.join(
        "backend/data/documents",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    state = {
        "company": company,
        "pdf_path": pdf_path,
        "query": query,
        "news": "",
        "financials": "",
        "legal": "",
        "risk": "",
        "report": "",
        "selected_agents": []
    }

    with st.spinner("Running Multi-Agent Due Diligence..."):

        result = graph.invoke(state)

    st.success("Analysis Complete!")

    st.divider()

    st.subheader("Generated Due Diligence Report")

    st.markdown(result["report"])

    st.download_button(
        "📥 Download Report",
        result["report"],
        file_name=f"{company}_Due_Diligence_Report.md",
        mime="text/markdown"
    )