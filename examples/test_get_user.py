from sof2ai.modules.users.repository import users_repository

user = users_repository.get_user(1)
print(user)