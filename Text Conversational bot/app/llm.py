
from langchain.schema import (
    SystemMessage,
    HumanMessage
)
from app.prompts import SYSTEM_PROMPT
from app.model import llm
from app.safety import detect_self_harm_risk
from app.safe_response import generate_safe_response
# ---------------------------------------
# BUILD CONVERSATION CONTEXT
# ---------------------------------------

def build_conversation_context(messages):

    if not messages:
        return ""

    formatted = []

    recent = messages[-8:]

    for msg in recent:

        role = msg["role"]

        if role == "user":

            formatted.append(
                f"User: {msg['message']}"
            )

        else:

            formatted.append(
                f"Friend: {msg['message']}"
            )

    return "\n".join(formatted)
# ---------------------------------------
# GENERATE RESPONSE
# ---------------------------------------

def generate_response(
    user_message: str,
    recent_messages: list
):

    conversation_context = build_conversation_context(
        recent_messages
    )
    # ------------------------------- 
    #  SAFETY CHECK 
    #  ------------------------------- 
    if detect_self_harm_risk(user_message):
        return generate_safe_response( 
            user_message
         )
    
    prompt = f"""
Previous conversation:
{conversation_context}

Current user message:
{user_message}

memory_summary = ""

Respond naturally.

IMPORTANT:

- Continue conversation naturally.
- Match emotional tone realistically.
- Avoid robotic empathy.
- Avoid over-explaining.
- Avoid repeating user words.
- Avoid emotional mirroring in every response.
- Avoid repetitive coping suggestions.
- If the user becomes irritated,
  reduce advice and respond more casually.
- If the user asks a direct question,
  answer it properly.
- Keep the flow realistic and human.
"""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)

    return response.content.strip()

