from pydantic import BaseModel
from datetime import datetime
from typing import List

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

class HistoryItem(BaseModel):
    timestamp: datetime
    prompt: str
    response: str

