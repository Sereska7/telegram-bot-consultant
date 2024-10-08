from pydantic import BaseModel


class CreateClient(BaseModel):
    tg_id: int
    user_name: str
    name: str
    number: str | None
