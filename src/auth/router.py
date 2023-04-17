from fastapi import APIRouter, Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm  # Это форма регистрации и авторизации

from auth.schemas import Token, UserCreate, User, BaseUser
from auth.services import AuthService, get_current_user


router = APIRouter(
    prefix='/core',
    tags=['core'],
)


@router.post('/signup/', response_model=BaseUser, status_code=status.HTTP_201_CREATED)
def sign_up(
    user_data: UserCreate,
    auth_service: AuthService = Depends(),
):
    return auth_service.register_new_user(user_data)


@router.post('/login/', response_model=Token)
def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends()):
    return AuthService.authenticate_user(
        auth_data.username,
        auth_data.password)


@router.get('/user/', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
