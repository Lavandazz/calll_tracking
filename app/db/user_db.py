from typing import Optional

from config.db.models import User


class UserDB:
    def __init__(self, session):
        self.session = session

    def get_user(self, username: str, hashed_password: str) -> Optional[User]:
        return self.session.query(User).filter(User.username == username, User.hashed_password == hashed_password).first()

    def create_user(self, username: str, hashed_password: str, email: str) -> User:
        new_user = User(username=username, hashed_password=hashed_password, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user