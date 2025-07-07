# Backend Development Intern Practical Test

A simple FastAPI backend application that allows users to:

* Log in using a hardcoded list of users
* Submit text prompts and get a dummy AI-style response
* Retrieve a history of their past prompts and responses

## Features

* Token-based authentication using Bearer tokens
* In-memory storage for user sessions and prompt history
* Clean FastAPI design with Pydantic models for validation
* Minimal dependencies and easy to run

---

## How to Run the App Locally

### Option A: Manual Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/backend-test-app.git
cd backend-test-app
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Access the docs at: `http://127.0.0.1:8000/docs`

### Option B: One-liner Quick Setup (Linux/macOS)

```bash
git clone https://github.com/your-username/backend-test-app.git && \
cd backend-test-app && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
uvicorn main:app --reload
```

---

## Example `curl` Commands

### 1. Log In

```bash
curl -X POST http://127.0.0.1:8000/login/ \
-H "Content-Type: application/json" \
-d '{"username": "alice", "password": "password123"}'
```

### 2. Submit a Prompt

```bash
curl -X POST http://127.0.0.1:8000/prompt/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"prompt": "What is the capital of France?"}'
```

### 3. Get Prompt History

```bash
curl -X GET http://127.0.0.1:8000/history/ \
-H "Authorization: Bearer <your_token>"
```

---

## Users (Hardcoded)

```json
{
  "alice": "password123",
  "bob": "secret"
}
```

---

## Folder Structure

```
backend-test-app/
├── main.py           # App entry point
├── auth.py           # Authentication and token logic
├── routes.py         # All route definitions
├── models.py         # Pydantic models
├── requirements.txt  # Dependencies
├── .gitignore        # Git exclusions
└── README.md         # Documentation
```
