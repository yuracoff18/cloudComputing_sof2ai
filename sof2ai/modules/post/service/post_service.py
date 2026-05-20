from sof2ai.modules.post.repository import post_repository
from sof2ai.modules.post.constants import post_constants

def create_post_service(title: str, content: str, user_id: int):
    if len(title) > post_constants.MAX_TITLE_LENGTH:
        raise Exception("Title too long")

    return post_repository.create_post(title, content, user_id)

def delete_post_service(post_id: int):
    return post_repository.delete_post(post_id)

def update_post_service(title: str, content: str, post_id:int):
    return post_repository.update_post(title, content, post_id)

def get_all_posts_service():
    return post_repository.get_all_posts()