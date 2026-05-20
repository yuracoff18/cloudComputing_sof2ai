from fastapi import APIRouter, HTTPException
from sof2ai.modules.users.schema.user_schema import UserCreate
from sof2ai.modules.users.service import users_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: UserCreate):
    try:
        return users_service.create_user_service(user.email, user.name, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}")
def get_user(user_id: int):
    try:
        return users_service.get_user_service(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete('/{user_id}')
def delete_user(user_id: int):
    try:
        return users_service.delete_user_service(user_id)
    except Exception as e:
        raise HTTPException(404, str(e))