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
    calls: Mapped[list["Call"]] = relationship(back_populates="user")

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


class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_company: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=True)

    name_vacancy: Mapped[str] = mapped_column(Text)
    requirements: Mapped[str] = mapped_column(Text, nullable=True)
    contact_person: Mapped[str] = mapped_column(Text, nullable=True)
    contact_phone: Mapped[str] = mapped_column(Text, nullable=True)
    contact_email: Mapped[str] = mapped_column(Text, nullable=True)
    link_vacancy: Mapped[str] = mapped_column(Text, nullable=True)
    date_create: Mapped[date] = mapped_column(Date, default=date.today)

    company: Mapped[Optional["Company"]] = relationship(back_populates="vacancies")
    calls: Mapped[list["Call"]] = relationship(back_populates="vacancy")
    


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_company: Mapped[str] = mapped_column(Text, unique=True)
    contact_person: Mapped[str] = mapped_column(Text, nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    phone: Mapped[str] = mapped_column(Text, nullable=True)
    email: Mapped[str] = mapped_column(Text, nullable=True)
    website: Mapped[str] = mapped_column(Text, nullable=True)
    date_create: Mapped[date] = mapped_column(Date, default=date.today)


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    name_candidate: Mapped[str] = mapped_column(Text)
    phone: Mapped[str] = mapped_column(Text, nullable=True)
    email: Mapped[str] = mapped_column(Text, nullable=True)
    link_resume: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)
    source: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # <-- добавлено
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    date_create: Mapped[date] = mapped_column(Date, default=date.today)

    calls: Mapped[list["Call"]] = relationship(back_populates="candidate")


class Call(Base):
    __tablename__ = "calls"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_candidate: Mapped[int] = mapped_column(ForeignKey("candidates.id"), nullable=True)
    id_vacancy: Mapped[int] = mapped_column(ForeignKey("vacancies.id"), nullable=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    date_call: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())
    duration_minutes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(Text, nullable=True)
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    link_resume: Mapped[str] = mapped_column(Text, nullable=True)

    candidate: Mapped[Optional["Candidate"]] = relationship(back_populates="calls")
    vacancy: Mapped[Optional["Vacancy"]] = relationship(back_populates="calls")
    user: Mapped[Optional["User"]] = relationship(back_populates="calls")