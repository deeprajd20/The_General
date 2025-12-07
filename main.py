from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from fastapi.middleware.cors import CORSMiddleware
# from src.api.router.api_router import api_router
# from api.router.home import router as home_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/frontend"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(api_router, prefix="/api")
# app.include_router(home_router)


@app.get("/")
def home():
    return FileResponse("src/frontend/index.html")

@app.get("/chat")
def chat_page():
    return FileResponse("src/frontend/chat.html")