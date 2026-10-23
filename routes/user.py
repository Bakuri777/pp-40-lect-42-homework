from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from repositories.user_repository import UserRepository
from schemas.user import UserCreate, UserResponse
from service.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(db: AsyncSession = Depends(get_db)):
    return UserService(UserRepository(db))


@router.get("/", response_model=list[UserResponse])
async def get_users(service: UserService = Depends(get_user_service)):
    return await service.get_all_user()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    return await service.get_user(user_id)


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return await service.create_user(data)
