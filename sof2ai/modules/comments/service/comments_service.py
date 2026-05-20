from sof2ai.modules.comments.repository import comments_repository
from sof2ai.modules.comments.constants import comments_constants

def create_comment_service(post_id: int, user_id: int, content: str, parent_comment_id: int | None):
    if len(content) > comments_constants.MAX_COMMENT_LENGTH:
        raise Exception("Comment too long")

    return comments_repository.create_comment(
        post_id,
        user_id,
        content,
        parent_comment_id
    )
    
def delete_comment_service(comment_id: int):
    if not comment_id:
        raise Exception("No es un id valido")
    return comments_repository.delete_comment(comment_id)

def update_comment_service(comment_id: int, content: str):
    return comments_repository.update_comment(content, comment_id)

def get_all_by_post_id_service(post_id: int):
    return comments_repository.get_all_by_post_id(post_id)