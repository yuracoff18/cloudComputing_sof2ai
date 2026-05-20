from sof2ai.modules.users.repository import users_repository


def create_user_service(email: str, name: str, password:str):
    existing_user = users_repository.get_user_by_email(email)

    if existing_user:
        raise Exception("User already exists")

    return users_repository.create_user(email, name, password)


def get_user_service(user_id: int):
    user = users_repository.get_user_by_id(user_id)

    if not user:
        raise Exception("User not found")

    return user

def delete_user_service(user_id: int):
    deleted = users_repository.delete_user(user_id)

    if not deleted:
        raise Exception('user not found')
    return deleted

