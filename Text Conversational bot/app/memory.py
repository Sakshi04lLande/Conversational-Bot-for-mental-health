from sqlalchemy.orm import Session
from app.models import Conversation


def save_message(
    db: Session,
    user_id: str,
    role: str,
    message: str
):

    msg = Conversation(
        user_id=user_id,
        role=role,
        message=message
    )

    db.add(msg)
    db.commit()


def get_recent_messages(
    db: Session,
    user_id: str,
    limit: int = 8
):

    messages = (
        db.query(Conversation)
        .filter(Conversation.user_id == user_id)
        .order_by(Conversation.created_at.desc())
        .limit(limit)
        .all()
    )

    messages.reverse()

    return [
        {
            "role": msg.role,
            "message": msg.message
        }
        for msg in messages
    ]