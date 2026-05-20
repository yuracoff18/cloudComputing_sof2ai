from pydantic import BaseModel

class CreatePostRequest(BaseModel):
    title: str
    content: str
    user_id: int
    
class UpdatePostRequest(BaseModel):
    post_id:int
    title: str
    content:str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: str