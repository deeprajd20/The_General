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
        self.current_in_live_memory = None
        self.messages = {}
           

        return None
    

    # def message_template():


    def _chat_config(self,user_query, system_prompt="You are a helpful AI assistant."):
        headers = {
            "Authorization": f"Bearer {self.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user_prompt", "content": user_query}
            ],
            "temperature": 0.3,
            "max_tokens": 1000
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
    
    def analytics_hub_cache(self):
        with open(self.cache_file_path,"r") as local_cache_file:
            file_content = local_cache_file.read()
            temp_file = json.loads(file_content)
            
        return temp_file    
    
    def _get_file_size(self):
        file_size = os.path.getsize(self.cache_file_path)
        file_size_in_mb = file_size / (1024 * 1024)
        return file_size_in_mb
            
    def interact(self,user_query):
        return_content = {}
        query_id,timestamp,chat_response = self._chat_config(user_query)
        self._update_cache(query_id,user_query,timestamp,chat_response)
        return_content['response'] = chat_response
        return_content['current_file_size'] = self._get_file_size()
        return return_content

            

