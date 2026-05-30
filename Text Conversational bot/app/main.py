from fastapi import FastAPI
from app.routes.chat import router as chat_router


app = FastAPI(

    title="Mental Health Conversational AI",

    version="1.0.0"
)



app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Multilingual Emotional AI Chatbot Running"
    }