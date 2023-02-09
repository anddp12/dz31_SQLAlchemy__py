from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Base(DeclarativeBase):
    pass


# Creating a class Departments
class Departments(Base):
    __tablename__ = "Departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    financing: Mapped[float] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Departments(id={self.id!r}, name={self.name!r}, financing={self.financing!r})"


# Creating a class Faculties
class Faculties(Base):
    __tablename__ = "Faculties"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    dean: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Faculties(id={self.id!r}, name={self.name!r}, dean={self.dean!r})"


# Creating a class Groups
Faculties
class Groups(Base):
    __tablename__ = "Groups"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int] = mapped_column()
    rating: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Groups#(id={self.id!r}, name={self.name!r}, rating={self.rating!r}, rating={self.year!r})"


# Creating a class Teachers
class Teachers(Base):
    __tablename__ = "Teachers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
    employmentDate: Mapped[str] = mapped_column()
    salary: Mapped[float] = mapped_column()
    premium: Mapped[float] = mapped_column(default=0)
    isAssistant: Mapped[int] = mapped_column(default=0)
    isProfessor: Mapped[int] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Teachers#(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, position={self.position!r}, employmentDate={self.employmentDate!r}, salary={self.salary!r}, premium={self.premium!r})"

engine = create_engine("sqlite:///Academy_db.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Filling the tables of Departments
with Session(engine) as session:
    department1 = Departments(name="Architecture", financing=31000.0)
    department2 = Departments(name="Architectural programming", financing=21000.0)
    department3 = Departments(name="Atomation", financing=21500.0)
    department4 = Departments(name="Computer Sciences", financing=19500.0)
    department5 = Departments(name="Management organization", financing=23000.0)
    department6 = Departments(name="Engineering", financing=11500.0)

session.add_all([department1, department2, department3, department4, department5, department6])
session.commit()


# Filling the tables of Faculties
with Session(engine) as session:
    faculty1 = Faculties(name="Architecture", dean="Miron Markevich")
    faculty2 = Faculties(name="Information technologies", dean="Alexander Petrakov")
    faculty3 = Faculties(name="Construction", dean="Viktor Skrypnyk")

session.add_all([faculty1, faculty2, faculty3])
session.commit()