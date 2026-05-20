from fastapi import APIRouter, HTTPException
from sof2ai.modules.post.schema.post_schema import CreatePostRequest, UpdatePostRequest
from sof2ai.modules.post.service import post_service

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_post(request: CreatePostRequest):
    try:
        return post_service.create_post_service(
            request.title,
            request.content,
            request.user_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{post_id}")
def delete_post(post_id: int):
    try:
        return post_service.delete_post_service(
            post_id
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.patch('/')
def update_post(request: UpdatePostRequest):
    try:
        return post_service.update_post_service(
            request.title,
            request.content,
            request.post_id
        )
    except Exception as e:
        raise HTTPException(404, str(e))
    
@router.get('/')
def get_all_posts():
    try:
        return post_service.get_all_posts_service()
    except Exception as e:
        raise HTTPException(404, str(e))
    