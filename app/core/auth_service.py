from app.utils.hash_pass import verify_password

from typing import Optional
from sqlalchemy.orm import sessionmaker
from app.db.user_db import UserDB
from app.core.context import AppContext
from config.db.models import User


class AuthService:
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker
        self.context = AppContext()

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Проверяет логин и пароль, возвращает пользователя или None.
        """
        with self.session_maker() as session:
            user_db = UserDB(session)
            user = user_db.get_user_by_username(username)
            if user and verify_password(password, user.hashed_password):
                return user
            return None

    def login(self, username: str, password: str) -> bool:
        """
        Выполняет вход: если успешно, устанавливает текущего пользователя в контекст.
        """
        user = self.authenticate(username, password)
        if user:
            self.context.current_user_id = user.id
            # Если есть роли, можно установить и роль
            if user.user_role and user.user_role.role:
                self.context.current_user_role = user.user_role.role.role
            else:
                self.context.current_user_role = 'user'  # по умолчанию
            return True
        return False

    def logout(self):
        """Выход: очищает данные пользователя в контексте"""
        self.context.current_user_id = None
        self.context.current_user_role = None

    def get_current_user(self) -> Optional[User]:
        """Возвращает объект текущего пользователя (если авторизован)"""
        user_id = self.context.current_user_id
        if user_id is None:
            return None
        with self.session_maker() as session:
            user_db = UserDB(session)
            return user_db.get_user_by_id(user_id)