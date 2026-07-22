from typing import Optional, List
from config.db.models import User


class UserDB:
    def __init__(self, session):
        self.session = session

    def get_all_users(self) -> List[User]:
        """Возвращает всех пользователей"""
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()

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