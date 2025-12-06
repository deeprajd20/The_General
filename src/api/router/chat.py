import os
from fastapi import APIRouter
from ...core.chat import Chatbot
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('groq_api_key')

router = APIRouter()
bot = Chatbot(groq_api_key=api_key)

@router.get("/")
def chat():
    response = bot.interact('what is os')
    return {"message":response}
