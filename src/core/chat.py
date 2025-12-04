import requests
import os
from dotenv import load_dotenv
import json
import uuid
from src.utils import formatted_date
# load env 
load_dotenv()
os.getenv("groq_api_key")

class Chatbot:

    def __init__(self,groq_api_key=None,Model_name = "llama-3.1-8b-instant"):
        self.BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
        self.GROQ_API_KEY =  groq_api_key
        self.MODEL_NAME = Model_name
        self.cache_file_path = "src/core/cache.json"
           

        return None
    

    def _chat_config(self,user_query, system_prompt="You are a helpful AI assistant."):
        headers = {
            "Authorization": f"Bearer {self.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            "temperature": 0.3,
            "max_tokens": 300
        }

        response = requests.post(self.BASE_URL, headers=headers, json=data)
        id = str(uuid.uuid4())
        time_stamp = formatted_date()
        response.raise_for_status()
        out = response.json()

        return id,time_stamp,out["choices"][0]["message"]["content"]
    
    def _update_vdb(self,prompt):
        pass

    def _update_cache(self,query_id,user_query,timestamp,chat_response):
        
        new_upsert = {"query_id":query_id,
                       "time_stamp":timestamp,
                       "prompt":user_query,
                       "response":chat_response}
        try:
            with open(self.cache_file_path,"r") as local_db:
                data = json.load(local_db)
                if not isinstance(data,list):
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_upsert)

        with open(file=self.cache_file_path,mode="w") as local_db:
            json.dump(data,local_db,indent=2)
        
        return None
            
    def interact(self,user_query):
        query_id,timestamp,chat_response = self._chat_config(user_query)
        self._update_cache(query_id,user_query,timestamp,chat_response)

        return chat_response

            

