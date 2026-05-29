
from langchain.schema import HumanMessage

from app.model import llm




def generate_user_summary(messages):

    conversation = "\n".join([
        f"{m['role']}: {m['message']}"
        for m in messages
    ])

    prompt = f"""
Based on this conversation, generate a very short memory summary.

Only include: 
- important personal identity details 
- conversational tone

Keep it extremely short.

Conversation:
{conversation}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content.strip()

