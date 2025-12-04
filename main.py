from src.services.auth_grok import groq_chat

answer = groq_chat(message="what is neural networks")

print(answer)