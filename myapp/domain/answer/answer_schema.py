from pydantic import BaseModel, field_validator
import datetime
from domain.user.user_schema import User
from typing import Union

class AnswerCreate(BaseModel):
    content : str

    @field_validator('content')
    def not_empty(cls,v):
        if not v or not v.strip():
            raise ValueError("값을 넣어주세요.")
        
        return v
    

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: Union[User,None]=None

    