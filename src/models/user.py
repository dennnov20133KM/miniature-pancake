from pydoc import stripid
from models.base import Base, uuid_pk
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[uuid_pk]
    first_name: Mapped[str] = mapped_column(String(32), doc="Имя")
    last_name: Mapped[str] = mapped_column(String(32), doc="Фамилия")
    email: Mapped[str] = mapped_column(String(32), doc="Электронная почта", unique=True)
    password: Mapped[str] = mapped_column(String(512), doc="Пароль")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, doc="Активен")
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, doc="Админ")
