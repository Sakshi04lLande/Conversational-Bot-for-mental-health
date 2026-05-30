


---
# Mental Health Conversational AI

A multilingual emotional support chatbot built using FastAPI and Azure OpenAI.

## Features

* Multilingual Support

  * English
  * Marathi
  * Hindi
  * Roman Marathi → Marathi
  * Roman Hindi → Hindi

* Human-like Conversations

  * Natural responses
  * Emotionally intelligent interaction
  * Context-aware conversation flow

* Safety System

  * Self-harm risk detection
  * Safe response generation
  * Mental health helpline information

* Azure OpenAI Integration

  * GPT-based conversational responses
  * Context-aware prompting

* API Security

  * API key authentication
  * Secure request validation

---

## Project Structure
```text
project/

├── app/
│   ├── auth.py
│   ├── config.py
│   ├── llm.py
│   ├── main.py
│   ├── model.py
│   ├── prompts.py
│   ├── safe_response.py
│   ├── safety.py
│   ├── schemas.py
│   └── routes/
│       └── chat.py
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd mental-health-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
AZURE_OPENAI_API_KEY=your_azure_openai_key

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

AZURE_OPENAI_DEPLOYMENT=gpt-4o

AZURE_OPENAI_API_VERSION=2024-02-15-preview

CONVERSATIONAL_BOT_API_KEY=your_secure_api_key
```

---

## Run Application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## API Documentation

Swagger UI

```text
http://localhost:8000/docs
```

Redoc

```text
http://localhost:8000/redoc
```

---

## Authentication

All chat endpoints require:

```http
X-API-Key: your_secure_api_key
```

---

## Chat Endpoint

### POST

```http
/api/chat
```

### Request

```json
{
  "user_id": "user123",
  "message": "मला खूप एकटं वाटतं",
  "conversation_history": [
    {
      "role": "user",
      "message": "हाय"
    },
    {
      "role": "assistant",
      "message": "हाय, कसा आहेस?"
    }
  ]
}
```

### Response

```json
{
  "response": "अरे, काय झालं? बोलायचं असेल तर सांग."
}
```

---

## Safety Layer

The chatbot automatically:

* Detects self-harm intent
* Detects suicidal ideation
* Generates safe responses
* Shares verified helpline details

---

## Technology Stack

* FastAPI
* Azure OpenAI
* LangChain
* Python
* Docker
* Uvicorn

---
## Author
Sakshi Lande
