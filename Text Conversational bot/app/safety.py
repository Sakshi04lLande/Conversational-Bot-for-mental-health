
from langchain.schema import HumanMessage
from app.model import llm


def detect_self_harm_risk(text):

    try:

        prompt = f"""
Classify the user's message.

The message may be in:
- English
- Hindi
- Marathi
- Roman Hindi
- Roman Marathi

Reply ONLY:

HIGH_RISK

or

SAFE

HIGH_RISK includes messages expressing:

- wanting to die
- suicide thoughts
- self-harm thoughts
- not wanting to live
- wanting life to end
- wanting to disappear forever
- wanting to leave the world
- wishing not to exist

Examples of HIGH_RISK:

English:
"I want to die"
"I don't want to live anymore"
"I want to disappear forever"

Hindi:
"मुझे मर जाना है"
"मुझे अब जीना नहीं है"

Roman Hindi:
"muze mar jana hai"
"muze is duniya me rahana nahi hai"
"muze ye duniya chhod deni hai"

Marathi:
"मला मरून जावंसं वाटतं"
"मला आता जगायचं नाही"

Roman Marathi:
"mala marun javasa vatata"
"mala ata jagaycha nahi"
"mala he jag sodun jaychi iccha aahe"

Everything else should be SAFE.

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

