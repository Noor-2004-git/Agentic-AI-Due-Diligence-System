from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.llm_service import ask_llm

app = FastAPI(
    title="AI Due Diligence Consultant",
    version="1.0.0"
)


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "AI Due Diligence Consultant"
    }


@app.post("/chat")
def chat(request: PromptRequest):

    answer = ask_llm(request.prompt)

    return {
        "response": answer
    }