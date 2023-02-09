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


class Group_Teacher(Base):
    __tablename__ = "Group_Teacher"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_group: Mapped[int] = mapped_column(ForeignKey("Group.id"))
    id_teacher: Mapped[int] = mapped_column(ForeignKey("Teacher.id"))


engine = create_engine("sqlite:///Academy_db.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Filling the tables of Department
with Session(engine) as session:
    department1 = Department(name="Architecture", financing=31000.0)
    department2 = Department(name="Architectural programming", financing=21000.0)
    department3 = Department(name="Atomation", financing=21500.0)
    department4 = Department(name="Computer Sciences", financing=19500.0)
    department5 = Department(name="Management organization", financing=23000.0)
    department6 = Department(name="Engineering", financing=11500.0)

session.add_all([department1, department2, department3, department4, department5, department6])
session.commit()


# Filling the tables of Facultie
with Session(engine) as session:
    faculty1 = Faculty(name="Architecture", dean="Miron Markevich")
    faculty2 = Faculty(name="Information technologies", dean="Alexander Petrakov")
    faculty3 = Faculty(name="Construction", dean="Viktor Skrypnyk")

session.add_all([faculty1, faculty2, faculty3])
session.commit()


# Filling the tables of Groups
with Session(engine) as session:
    group1 = Group(name="Architecture_5", year=5, rating=2)
    group2 = Group(name="Engineering_5", year=5, rating=5)
    group3 = Group(name="Computer Sciences_4", year=4, rating=1)
    group4 = Group(name="Management organization_4", year=4, rating=4)
    group5 = Group(name="Engineering_4", year=4, rating=3)
    group6 = Group(name="Computer Sciences_3", year=3, rating=6)
    group7 = Group(name="Engineering_2", year=2, rating=7)
    group8 = Group(name="Atomation_2", year=2, rating=8)
    group9 = Group(name="Engineering_1", year=1, rating=9)
    group10 = Group(name="Architectural programming_1", year=1, rating=10)

session.add_all([group1, group2, group3, group4, group5, group6, group7, group8, group9, group10])
session.commit()


# Filling the tables of Teacher
with Session(engine) as session:
    teacher1 = Teacher(first_name="Alexander", last_name="Svatok", position="Assistant", employmentDate="2013-03-18", salary=7500.0, premium=435.0, isAssistant=1, isProfessor=0)
    teacher2 = Teacher(first_name="Eugene", last_name="Cheberyachko", position="Docent", employmentDate="2012-09-31", salary=11500.0, premium=1205.0, isAssistant=0, isProfessor=0)
    teacher3 = Teacher(first_name="Artem", last_name="Fedetskyi", position="Professor", employmentDate="2010-07-21", salary=13500.0, premium=935.0, isAssistant=0, isProfessor=1)
    teacher4 = Teacher(first_name="Dmitry", last_name="Chygrinsky", position="Docent", employmentDate="2011-05-28", salary=11500.0, premium=868.0, isAssistant=0, isProfessor=0)
    teacher5 = Teacher(first_name="Nikolai", last_name="Kalynych", position="Docent", employmentDate="2014-07-11", salary=11500.0, premium=1195.0, isAssistant=0, isProfessor=0)
    teacher6 = Teacher(first_name="Yevgeny", last_name="Konoplyanka", position="Senior teacher", employmentDate="2011-02-12", salary=9500.0, premium=842.0, isAssistant=0, isProfessor=0)
    teacher7 = Teacher(first_name="Yevgeny", last_name="Selezgnev", position="Professor", employmentDate="2012-11-02", salary=13500.0, premium=632.0, isAssistant=0, isProfessor=1)
    teacher8 = Teacher(first_name="Igor", last_name="Vartsaba", position="Assistant", employmentDate="2020-09-14", salary=8000.0, premium=789.0, isAssistant=1, isProfessor=0)
    teacher9 = Teacher(first_name="Roman", last_name="Zozulya", position="Professor", employmentDate="2010-03-07", salary=13500.0, premium=1185.0, isAssistant=0, isProfessor=1)
    teacher10 = Teacher(first_name="Roman", last_name="Bezus", position="Senior teacher", employmentDate="2013-10-15", salary=9500.0, premium=1365.0, isAssistant=0, isProfessor=0)
    teacher11 = Teacher(first_name="Yevgeny", last_name="Shakhov", position="Assistant", employmentDate="2020-05-16", salary=8500.0, premium=1035.0, isAssistant=1, isProfessor=0)
    teacher12 = Teacher(first_name="Denis", last_name="Boyko", position="Senior teacher", employmentDate="2013-08-23", salary=9500.0, premium=895.0, isAssistant=0, isProfessor=0)

session.add_all([teacher1, teacher2, teacher3, teacher4, teacher5, teacher6, teacher7, teacher8, teacher9, teacher10, teacher11, teacher12])
session.commit()