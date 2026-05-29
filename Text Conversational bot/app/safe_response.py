
from langchain.schema import HumanMessage
from app.model import llm


SUPPORT_MESSAGE = """

If things feel too overwhelming right now,
you can also reach out here:

Helpline:
8448440632

Email:
manodarpan-mhrd@gov.in

Website:
https://manodarpan.education.gov.in/

"""


def generate_safe_response(user_message):

    prompt = f"""
The user may be emotionally overwhelmed.

Respond like a calm, emotionally mature human friend.

IMPORTANT:

- Reply in the SAME language as the user.
- If the user writes Marathi or Hindi in Roman script,
  reply in natural Devanagari script.
- Keep the response short and natural.
- Sound grounded, calm, and human.
- Avoid therapy tone.
- Avoid motivational language.
- Avoid dramatic emotional support.
- Avoid generic reassurance.
- Avoid sounding scripted.
- Do not lecture the user.
- Do not panic.
- Do not overreact.
- Never encourage harmful behavior.

IMPORTANT:

- The goal is to emotionally slow down the conversation.
- Keep emotional intensity calm and stable.
- Respond naturally like a caring human.

IMPORTANT LANGUAGE RULE:

- If the user message is English,
  reply ONLY in English.

- If the user message is Marathi written in English letters,
  reply ONLY in Devanagari Marathi.

- If the user message is Hindi written in English letters,
  reply ONLY in Devanagari Hindi.

- Never mix languages.



User message:
{user_message}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    final_response = response.content.strip()

    final_response += SUPPORT_MESSAGE

    return final_response

