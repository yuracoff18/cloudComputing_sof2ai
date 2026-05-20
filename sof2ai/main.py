from fastapi import FastAPI
from sof2ai.modules.users.controller import users_controller
from sof2ai.modules.post.controller import post_controller
from sof2ai.modules.comments.controller import comments_controller

app = FastAPI()

app.include_router(users_controller.router)
app.include_router(post_controller.router)
app.include_router(comments_controller.router)