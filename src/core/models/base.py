from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Данный метод автоматически генерирует имя таблицы для класса модели.
        Имя таблицы будет соответствовать имени класса в нижнем регистре и с суффиксом 's'.

        Например, для класса `User` имя таблицы будет `users`.
        """
        return f"{cls.__name__.lower()}s"

    # Основное поле `id`, которое является первичным ключом во всех моделях, наследуемых от Base.
    id: Mapped[int] = mapped_column(primary_key=True)


