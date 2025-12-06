import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    welcome_string = "THIS is an Chatbot" 
    return welcome_string
