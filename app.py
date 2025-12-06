import os
from src.core.chat import Chatbot

bot = Chatbot(groq_api_key=os.getenv("groq_api_key"))

while True:
    text = input("You: ")
    if text == "exit":
        break
    reply = bot.interact(text)
    print("Bot:",reply['response'] )