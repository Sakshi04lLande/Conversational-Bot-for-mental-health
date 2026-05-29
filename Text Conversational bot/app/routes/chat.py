from fastapi import (
    APIRouter,
    Depends
)

from fastapi import (
    APIRouter,
    Depends
)
from app.auth import verify_api_key


from sqlalchemy.orm import Session

from app.schemas import (
    ChatRequest,
    ChatResponse
)

from app.database import SessionLocal

from app.memory import (
    save_message,
    get_recent_messages
)

from app.llm import generate_response

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.post(
    "/chat",
    response_model=ChatResponse,
    dependencies=[Depends(verify_api_key)]
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    # normalize user id
    user_id = request.user_id.strip().lower()

    recent_messages = get_recent_messages(
        db,
        user_id
    )

    response = generate_response(
        user_message=request.message,
        recent_messages=recent_messages
    )

    save_message(
        db,
        user_id,
        "user",
        request.message
    )

    save_message(
        db,
        user_id,
        "assistant",
        response
    )

    return ChatResponse(
        response=response
    )

