from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr, field_validator
import re

app = FastAPI()

# Basemodel for APIs
class TimeModel(BaseModel):
    time: str

    @field_validator("time")
    @classmethod
    def validate_time_format(cls, v):
        if not re.match(r"^[0-2]\d[0-5]\d$", v):
            raise ValueError("Time must be in hhmm format")
        return v


class Instructor(BaseModel):
    name: str
    email: EmailStr


class Course(BaseModel):
    title: str
    description: str
    start: TimeModel
    end: TimeModel
    instructor: Instructor

class Error(BaseModel):
    error: bool
    msg: str

# Course List API
@app.get('/courses', response_model=Course, responses={
    200: {"model": Course, "description": "Successful of returning courses."},
    422: {"model": Error, "description": ""}
})