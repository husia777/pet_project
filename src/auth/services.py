from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt


from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from auth import models, schemas


from database import get_session
from config_app import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in/')

def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    return AuthService.verify_token(token)

class AuthService:
    # создание подключения
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    @classmethod
    # Функция валидации пароля проверяет пароль который приходит из формы с паролем в бд
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    # Функция хеширования  пароля 
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    # Функция валидации токена который пришел из запроса 
    def verify_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'})

        try:  	# Достаем данные из токена
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm])
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    # Создание токена из пользователя
    def create_token(cls, user: models.User) -> schemas.Token:
        user_data = schemas.User.from_orm(user)    # превращаем модель орм в модель pydantic
        now = datetime.utcnow()
        # формируем токен
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expires_s),
            'sub': str(user_data.id),
            'user': user_data.dict()}

        # создаем токен
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm)
        # Возвращаем токен на основе модели pydantic
        return schemas.Token(access_token=token)

    # Создаем юзера
    async def register_new_user(self, user_data: schemas.UserCreate,) -> schemas.BaseUser:
        if user_data.password == user_data.password_repeat:
            user = models.User(
                name=user_data.name,
                surname=user_data.surname,
                email=user_data.email,
                username=user_data.username,
                hashed_password=self.hash_password(user_data.password))
            self.session.add(user)
            await self.session.commit()
            return schemas.BaseUser(username=user.username, email=user.email)

    def authenticate_user(self, username: str, password: str) -> schemas.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'})
        user = select(models.User).where(models.User.username == username)
        if not user:
            raise exception
        if not self.verify_password(password, user.password_hash):
            raise exception
        return self.create_token(user)
