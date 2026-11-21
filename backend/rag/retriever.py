from backend.rag.vector_store import create_vector_store
from backend.rag.loader import load_pdf
from backend.rag.splitter import split_documents


def retrieve_documents(pdf_path, query):

    docs = load_pdf(pdf_path)

    chunks = split_documents(docs)

    vector_store = create_vector_store(chunks)

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    results = retriever.invoke(query)

    return results