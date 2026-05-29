
from langchain.schema import HumanMessage
from app.model import llm


def detect_self_harm_risk(text):

    try:

        prompt = f"""
Classify this message.

Reply ONLY:
SAFE
or
HIGH_RISK

Message:
{text}
"""

        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        result = response.content.strip()

        return result == "HIGH_RISK"

    except Exception:

        # If Azure blocks request,
        # assume HIGH_RISK for safety

        return True

