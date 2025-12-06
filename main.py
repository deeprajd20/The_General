import os
from dotenv import load_dotenv
from src.core.chat import Chatbot
load_dotenv()

# init chatbot
bot = Chatbot(groq_api_key=os.getenv("groq_api_key"))
print(bot.current_in_live_memory==None)

# response = bot.interact("what is a computer tell me about its different components and describe each and every components")
# print(response['current_file_size'])