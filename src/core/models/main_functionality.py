from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models import BotOrder
from src.core.models.base import Base

if TYPE_CHECKING:
    from src.core.models import BotOrder


class MainFunctionality(Base):
    name: Mapped[str]
    description: Mapped[str]
