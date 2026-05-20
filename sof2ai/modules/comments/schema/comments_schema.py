from pydantic import BaseModel
from typing import Optional

class CreateCommentRequest(BaseModel):
    post_id: int
    user_id: int
    content: str
    parent_comment_id: Optional[int] = None
    
class UpdateCommentRequest(BaseModel):
    content: str
    comment_id: int

class CommentResponse(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    parent_comment_id: Optional[int]
    status: str
    created_at: str