from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Departments(Base):
    __tablename__ = "Departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    financing: Mapped[float] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Departments(id={self.id!r}, name={self.name!r}, financing={self.financing!r})"


class Faculties(Base):
    __tablename__ = "Faculties"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    dean: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Faculties(id={self.id!r}, name={self.name!r}, dean={self.dean!r})"


class Groups(Base):
    __tablename__ = "Groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int] = mapped_column()
    rating: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Groups#(id={self.id!r}, name={self.name!r}, rating={self.rating!r}, rating={self.year!r})"