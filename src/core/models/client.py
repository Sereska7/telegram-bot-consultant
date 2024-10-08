from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models.base import Base

if TYPE_CHECKING:
    from src.core.models import BotOrder


class Client(Base):

    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    user_name: Mapped[str]
    name: Mapped[str]
    number: Mapped[str] = mapped_column(nullable=True)

    order: Mapped["BotOrder"] = relationship(back_populates="user")
