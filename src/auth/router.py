from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm  # Это форма регистрации и авторизации
from auth.schemas import Token, UserCreate, User, BaseUser, UserUpdate
from auth.services import AuthService, get_current_user
from fastapi.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
router = APIRouter(
    prefix='/core',
    tags=['core'],
)


@router.post('/signup/', response_model=BaseUser, status_code=status.HTTP_201_CREATED)
async def sign_up(
        user_data: UserCreate,
        auth_service: AuthService = Depends(),
):
    return await auth_service.register_new_user(user_data)


@router.post('/login/', response_model=Token)
async def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends()):
    return await auth_service.authenticate_user(
        auth_data.username,
        auth_data.password)


@router.get("/logout/")
async def logout():
    response = Response(status_code=HTTP_204_NO_CONTENT)
    response.delete_cookie(key='access_token')
    return response


@router.get('/profile/', response_model=User)
async def get_user(user: User = Depends(get_current_user)):
    return user


@router.put('/profile/', response_model=User)
async def update_user(user_data: UserUpdate, user: User = Depends(get_current_user),
                      auth_service: AuthService = Depends()):
    return await auth_service.change_user(user_data, user)
