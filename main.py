# import os
# from src.core.chat import Chatbot

# bot = Chatbot(groq_api_key=os.getenv("groq_api_key"))

# while True:
#     text = input("You: ")
#     if text == "exit":
#         break
#     reply = bot.interact(text)
#     print("Bot:",reply['response'] )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router.api_router import api_router
from src.api.router.home_router import router as home_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api")
app.include_router(home_router)