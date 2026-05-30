from fastapi import (
    APIRouter,
    Depends
)

from app.auth import verify_api_key

from app.schemas import (
    ChatRequest,
    ChatResponse
)

from app.llm import generate_response

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
    dependencies=[Depends(verify_api_key)]
)
def chat(
    request: ChatRequest
):

    user_id = request.user_id.strip().lower()

    recent_messages = [
        {
            "role": msg.role,
            "message": msg.message
        }
        for msg in request.conversation_history
    ]

    response = generate_response(
        user_message=request.message,
        recent_messages=recent_messages
    )

    return ChatResponse(
        response=response
    )