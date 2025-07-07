import uuid
from fastapi import HTTPException, Header
from typing import Optional

# Hardcoded users
users = {
    "alice": "password123",
    "bob": "secret"
}

# In-memory token storage
tokens = {}

def authenticate_user(username: str, password: str) -> str:
    if users.get(username) == password:
        token = str(uuid.uuid4())
        tokens[token] = username
        return token
    raise HTTPException(status_code=401, detail="Invalid username or password")

def get_current_user(authorization: Optional[str] = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    
    token = authorization.split(" ")[1]
    if token not in tokens:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return tokens[token]
