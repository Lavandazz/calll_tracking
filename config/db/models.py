from datetime import date, datetime
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, Integer, Text, TIMESTAMP, func, BigInteger

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(Text, unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(Text)
    username: Mapped[str] = mapped_column(Text)
    telephone: Mapped[str] = mapped_column(Text, nullable=True)
    
    # связь с ролями через таблицу user_roles
    user_role: Mapped[Optional["UserRole"]] = relationship(back_populates="user")
    
    def __repr__(self) -> str: # вывод в консоль для отладки
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.email!r})"
    
    def __str__(self) -> str: # строковое представление для удобства чтения (логгер)
            return f"Пользователь {self.id}, username {self.username}"



class Role(Base):
    """
    Модель роли (Админ, Пользователь)
    """
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(Text, unique=True)  # "admin", "user"

    # связь с пользователями через таблицу user_roles
    # list используется, так как одна роль может быть у нескольких пользователей
    user_roles: Mapped[list["UserRole"]] = relationship(back_populates="role")


class UserRole(Base):
    """
    Связь пользователя и роли
    """
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)  # Один пользователь может иметь только одну роль
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
 
    # user_role - связь с пользователем, back_populates указывает на атрибут в модели User, который ссылается на эту модель
    # role - связь с ролью, back_populates указывает на атрибут в модели Role, который ссылается на эту модель
    user: Mapped[User] = relationship(back_populates="user_role")
    role: Mapped["Role"] = relationship(back_populates="user_roles")  


