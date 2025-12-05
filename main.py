import os
from dotenv import load_dotenv
from src.core.chat import Chatbot
from fastapi import FastAPI


load_dotenv()

api_key = os.getenv("groq_api_key")

bot = Chatbot(groq_api_key=api_key)

response = bot.interact('what is database')
print(response)
