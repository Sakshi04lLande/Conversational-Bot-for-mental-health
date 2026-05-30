
from pydantic import BaseModel


class ConversationMessage(BaseModel):
    role: str
    message: str


class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_history: list[ConversationMessage] = []


class ChatResponse(BaseModel):
    response: str

