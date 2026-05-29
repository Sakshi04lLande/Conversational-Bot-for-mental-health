# Multilingual Emotional Conversational AI API

## Overview

Multilingual Emotional Conversational AI is a FastAPI-based chatbot API that provides natural, context-aware conversations in multiple languages.

The chatbot supports:

* English
* Marathi
* Hindi

The system maintains conversation history, generates context-aware responses, performs emotional risk detection, and provides safer responses when users appear emotionally overwhelmed.

The project uses Azure OpenAI for response generation and PostgreSQL for conversation memory storage.

---

# Features

## Conversational AI

* Context-aware conversations
* Human-like conversational style
* Multilingual support
* Conversation memory
* Natural emotional conversations

---

## Safety System

* Emotional risk detection
* Self-harm risk classification
* Safe response generation
* Support resource sharing

---

## Authentication

* API Key Authentication
* Swagger UI authorization support
* Protected endpoints

---

## Technology Stack

### Backend

* FastAPI
* Python 3.11

### AI

* Azure OpenAI
* LangChain

### Database
* PostgreSQL

### ORM
* SQLAlchemy

### Containerization

* Docker
* Docker Compose

---

# Project Structure

```text
project/

├── app/
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── llm.py
│   ├── main.py
│   ├── memory.py
│   ├── memory_summary.py
│   ├── model.py
│   ├── models.py
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

# Environment Variables

Create a `.env` file.

```env
AZURE_OPENAI_API_KEY=your_api_key

AZURE_OPENAI_ENDPOINT=your_endpoint

AZURE_OPENAI_DEPLOYMENT=your_deployment

AZURE_OPENAI_API_VERSION=your_version

DATABASE_URL=postgresql://postgres:postgres@postgres:5432/conversational_ai

CONVERSATIONAL_BOT_API_KEY=your_secure_api_key
```

---

# Local Development Setup

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload --port 8015
```

---

# Docker Setup

## Build Containers

```bash
docker compose build
```

---

## Start Containers

```bash
docker compose up -d
```

---

## View Logs

API Logs

```bash
docker logs -f conversational_ai_api
```

PostgreSQL Logs

```bash
docker logs -f conversational_postgres
```

---

## Stop Containers

```bash
docker compose down
```

---

## Rebuild After Changes

```bash
docker compose up --build
```

---

# PostgreSQL

## PostgreSQL Container

Container Name:

```text
conversational_postgres
```

Database:

```text
conversational_ai
```

User:

```text
postgres
```

Password:

```text
postgres
```

Host:

```text
localhost
```

Port:

```text
5435
```

---

## Connect To PostgreSQL

```bash
docker exec -it conversational_postgres psql -U postgres -d conversational_ai
```

---

## View All Conversations

```sql
SELECT *
FROM conversations;
```

---

## View User Conversation

```sql
SELECT role,
       message,
       created_at
FROM conversations
WHERE user_id='user123'
ORDER BY created_at ASC;
```

---

## View All User IDs

```sql
SELECT DISTINCT user_id
FROM conversations;
```

---

## Delete All Conversations

```sql
TRUNCATE TABLE conversations RESTART IDENTITY;
```

---

# Swagger UI

Open:

```text
http://localhost:8015/docs
```

---

## Authorize API

Click:

```text
Authorize
```

Enter:

```text
X-API-Key
```

Value:

```text
your_secure_api_key
```

Click:

```text
Authorize
```

---

# API Endpoint

## Chat

### Endpoint

```http
POST /chat
```

### Request

```json
{
  "user_id": "user123",
  "message": "Hi, I want to talk."
}
```

### Response

```json
{
  "response": "Hi, what's on your mind?"
}
```

---

# How To Use API Using Python

```python
import requests

url = "http://localhost:8015/chat"

payload = {
    "user_id": "user123",
    "message": "Hi, I want to talk."
}

headers = {
    "X-API-Key": "your_secure_api_key"
}

response = requests.post(
    url,
    json=payload,
    headers=headers
)

print(response.json())
```

---

# API Health Check

### Endpoint

```http
GET /
```

### Response

```json
{
  "message": "Multilingual Emotional AI Chatbot Running"
}
```

---

# Safety Workflow

1. User sends message.
2. Risk classifier evaluates message.
3. If SAFE:

   * Normal conversational response generated.
4. If HIGH_RISK:

   * Safe response generated.
   * Support resources provided.
5. Response stored in database.

---

# Database Tables

## conversations

Stores complete conversation history.

| Column     | Type     |
| ---------- | -------- |
| id         | Integer  |
| user_id    | String   |
| role       | String   |
| message    | Text     |
| created_at | DateTime |

---

## user_memory

Stores user memory summaries.

| Column  | Type    |
| ------- | ------- |
| id      | Integer |
| user_id | String  |
| summary | Text    |

---


# Author
Sakshi Lande
