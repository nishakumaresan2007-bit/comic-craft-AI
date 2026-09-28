from pydantic import BaseModel

class StoryRequest(BaseModel):
    prompt: str
    genre: str = "adventure"