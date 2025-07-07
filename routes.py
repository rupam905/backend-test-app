from fastapi import APIRouter, Depends
from datetime import datetime
import random

from models import LoginRequest, LoginResponse, PromptRequest, PromptResponse, HistoryItem
from auth import authenticate_user, get_current_user

router = APIRouter()

# In-memory storage of user prompt history
user_histories = {}

fake_responses = [
    "Interesting... Let's explore that idea.",
    "Let me think...",
    "Good question!",
    "That sounds intriguing.",
    "I'll get back to you on that.",
    "Hmmm, processing..."
]

@router.post("/login/", response_model=LoginResponse)
def login(data: LoginRequest):
    token = authenticate_user(data.username, data.password)
    return {"token": token}

@router.post("/prompt/", response_model=PromptResponse)
def submit_prompt(data: PromptRequest, username: str = Depends(get_current_user)):
    response = random.choice(fake_responses)
    timestamp = datetime.now()

    entry = HistoryItem(
        timestamp=timestamp,
        prompt=data.prompt,
        response=response
    )

    if username not in user_histories:
        user_histories[username] = []
    
    user_histories[username].append(entry)
    return {"response": response}

@router.get("/history/", response_model=list[HistoryItem])
def get_history(username: str = Depends(get_current_user)):
    return user_histories.get(username, [])
