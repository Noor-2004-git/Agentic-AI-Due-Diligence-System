

from backend.rag.retriever import retrieve_documents

pdf_path = "backend/data/documents/MSFT_FY25q4_10K.pdf"

query = "What does Microsoft say about Artificial Intelligence?"

results = retrieve_documents(pdf_path, query)

print("\n========== RETRIEVED DOCUMENTS ==========\n")

for i, doc in enumerate(results, start=1):
    print(f"\n---------- Chunk {i} ----------\n")
    print(doc.page_content)
    print("\n" + "=" * 80)