from typing import Optional, List
from config.db.models import User, UserRole
from sqlalchemy.orm import joinedload


class UserDB:
    def __init__(self, session):
        self.session = session

    def get_all_users(self) -> List[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_username(self, username: str) -> Optional[User]:
        """Возвращает пользователя по имени с подгрузкой роли."""
        return (self.session.query(User)
                .options(joinedload(User.user_role).joinedload(UserRole.role))
                .filter(User.username == username)
                .first())
    def create_user(self, user_data: dict) -> User:
        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update_user(self, user_id: int, update_data: dict) -> Optional[User]:
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            self.session.commit()
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False