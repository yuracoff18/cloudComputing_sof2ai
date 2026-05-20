from fastapi import APIRouter, HTTPException
from sof2ai.modules.comments.schema.comments_schema import CreateCommentRequest, UpdateCommentRequest
from sof2ai.modules.comments.service import comments_service

router = APIRouter(prefix="/comments", tags=["Comments"])

@router.post("/")
def create_comment(request: CreateCommentRequest):
    try:
        return comments_service.create_comment_service(
            request.post_id,
            request.user_id,
            request.content,
            request.parent_comment_id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete('/{comment_id}')
def delete_comment(comment_id: int):
    try:
        return comments_service.delete_comment_service(comment_id)
    except Exception as e:
        raise HTTPException(404, str(e))
    
@router.patch("/")
def update_comment(request: UpdateCommentRequest):
    try:
        return comments_service.update_comment_service(
            request.comment_id,
            request.content
        )
    except Exception as e:
        raise HTTPException(404, str(e))
    
@router.get('/{post_id}')
def get_all_by_post_id(post_id: int):
    try:
        return comments_service.get_all_by_post_id_service(post_id)
    except Exception as e:
        raise HTTPException(404, str(e))
