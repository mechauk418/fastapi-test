from typing import Union

from fastapi import FastAPI
from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)