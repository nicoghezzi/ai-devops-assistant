from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Question(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/ask")
def ask_ai(question: Question):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a DevOps assistant."
            },
            {
                "role": "user",
                "content": question.prompt
            }
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }