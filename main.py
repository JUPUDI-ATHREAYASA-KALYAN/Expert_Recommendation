from fastapi import FastAPI
from query import query
from user import user

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(query.query_router)
app.include_router(user.user_router)

origins = [
    "https://ers-7sjs.onrender.com/",
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:4200/",
    "https://ers-7sjs.onrender.com",
    "https://ers-7sjs"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("Yes")
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)


@app.get("/")
def index():
    return {"message":"Hello!"}


@app.get("/inservice")
def inservice():
    return True
