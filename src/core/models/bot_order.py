from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, DateTime, func, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models.base import Base

if TYPE_CHECKING:
    from src.core.models import Client, MainFunctionality, AdditionalService


class BotOrder(Base):
    client_tg_id: Mapped[int] = mapped_column(ForeignKey("clients.tg_id"))  # ID клиента в Telegram
    bot_purpose: Mapped[str] = mapped_column(String, nullable=False)  # Цель бота
    functionalities: Mapped[list[int]] = mapped_column(JSON, nullable=False)  # Список ID основных функций
    additional_services: Mapped[list[int]] = mapped_column(JSON, nullable=False)  # Список ID дополнительных услуг
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now())  # Время создания заявки

    user: Mapped["Client"] = relationship(back_populates="order")
