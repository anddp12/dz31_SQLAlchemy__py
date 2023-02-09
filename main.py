from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


# Creating a class Departments
class Department(Base):
    __tablename__ = "Department"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    financing: Mapped[float] = mapped_column(default=0)

    def __repr__(self) -> str:
        return f"Department(id={self.id!r}, name={self.name!r}, financing={self.financing!r})"


# Creating a class Faculty
class Faculty(Base):
    __tablename__ = "Faculty"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    dean: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Faculty(id={self.id!r}, name={self.name!r}, dean={self.dean!r})"


# Creating a class Group
class Group(Base):
    __tablename__ = "Group"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int] = mapped_column()
    rating: Mapped[int] = mapped_column()

    teachers: Mapped[list["Teacher"]] = relationship(secondary="Group_Teacher", back_populates="groups")

    def __repr__(self) -> str:
        return f"Group#(id={self.id!r}, name={self.name!r}, rating={self.rating!r}, rating={self.year!r})"


# Creating a class Teacher
class Teacher(Base):
    __tablename__ = "Teacher"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
    employmentDate: Mapped[str] = mapped_column()
    salary: Mapped[float] = mapped_column()
    premium: Mapped[float] = mapped_column(default=0)
    isAssistant: Mapped[int] = mapped_column(default=0)
    isProfessor: Mapped[int] = mapped_column(default=0)

    groups: Mapped[list["Group"]] = relationship(secondary="Group_Teacher", back_populates="teachers")

    def __repr__(self) -> str:
        return f"Teacher#(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, position={self.position!r}, employmentDate={self.employmentDate!r}, salary={self.salary!r}, premium={self.premium!r})"


# Creating a linking table Group_Teacher
class Group_Teacher(Base):
    __tablename__ = "Group_Teacher"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_group: Mapped[int] = mapped_column(ForeignKey("Group.id"))
    id_teacher: Mapped[int] = mapped_column(ForeignKey("Teacher.id"))


engine = create_engine("sqlite:///Academy_db.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# many to many Group_Teacher
with Session(engine) as session:
    groups1 = []
    groups1.append(Group(name="Engineering_5", year=5, rating=5))
    groups1.append(Group(name="Management organization_4", year=4, rating=1))
    groups1.append(Group(name="Engineering_4", year=4, rating=3))
    groups1.append(Group(name="Computer Sciences_3", year=3, rating=4))
    groups1.append(Group(name="Architectural programming_5", year=5, rating=2))
    teacher1 = Teacher(first_name="Nikolai", last_name="Kalynych", position="Docent", employmentDate="2014-07-11", salary=11500.0, premium=1195.0, isAssistant=0, isProfessor=0, groups=groups1)
    teacher2 = Teacher(first_name="Igor", last_name="Vartsaba", position="Assistant", employmentDate="2020-09-14", salary=8000.0, premium=789.0, isAssistant=1, isProfessor=0)
    teacher3 = Teacher(first_name="Roman", last_name="Bezus", position="Senior teacher", employmentDate="2013-10-15", salary=9500.0, premium=1365.0, isAssistant=0, isProfessor=0)
    teacher4 = Teacher(first_name="Denis", last_name="Boyko", position="Senior teacher", employmentDate="2013-08-23", salary=9500.0, premium=895.0, isAssistant=0, isProfessor=0)
    teacher5 = Teacher(first_name="Yevgeny", last_name="Selezgnev", position="Professor", employmentDate="2012-11-02", salary=13500.0, premium=632.0, isAssistant=0, isProfessor=1, groups=groups1)

    session.add_all(groups1)
    session.add_all((teacher1, teacher2, teacher3, teacher4, teacher5))
    session.commit()