from main import Group, Department, Teacher, Faculty, session


# Задание 1
# Вывести таблицу кафедр, но расположить ее поля в обратном порядке.

question1 = session.query(Department).filter(
    Department.id).order_by(Department.id.desc()).limit(10).all()

# print(question1)

# Задание 2
#  Вывести названия групп и их рейтинги с уточнением имен полей именем таблицы.

question2 = session.query(Group.name, Group.rating).order_by(
    Group.rating.desc()).limit(10).all()

# print(question2)

# Задание 5
# Вывести фамилии преподавателей, которые являются профессорами и ставка которых превышает 1050.

question5 = session.query(Teacher).filter((
    Teacher.salary>1050) & (Teacher.isProfessor == 1)).all()

# print(question5)

# Задание 6. Вывести названия кафедр, фонд финансирования от 11600 до 25000.

question6 = session.query(Department).filter((
    Department.financing >= 11600) & (Department.financing <=25000)).all()

# print(question6)

# Задание 7. Вывести названия факультетов кроме факультета “Информационных технологий”

question7 = session.query(Faculty).filter(
    Faculty.name != "Computer Sciences").all()

# print(question7)

# Задание 8. Вывести фамилии и должности преподавателей, которые не являются профессорами

question8 = session.query(Teacher.last_name, Teacher.position).filter(
    Teacher.isProfessor == 0).all()

# print(question8)

# Задание 9. Вывести фамилии, должности, ставки и надбавки ассистентов, у которых надбавка в диапазоне от 550 до 1500.

question9 = session.query(Teacher.last_name, Teacher.position, Teacher.salary, Teacher.premium).filter(
    (Teacher.isAssistant == 1) & 
    (Teacher.premium.between(550, 1550))).all()

# print(question9)

# Задание 10. Вывести фамилии и ставки ассистентов.

question10 = session.query(Teacher.last_name, Teacher.salary).filter(Teacher.isAssistant == 1).all()

# print(question10)

# Задание 13. Вывести фамилии ассистентов, имеющих зарплату (сумма ставки и надбавки) не более 8000.
question13 = session.query(Teacher.last_name).filter(
    Teacher.isAssistant == 1).filter((
        Teacher.salary + Teacher.premium)<=8000).all()

# print(question13)

# Задание 14. Вывести названия групп 5-го курса, имеющих рейтинг в диапазоне от 2 до 4

question14 = session.query(Group.name).filter((
    Group.rating.between(2, 4)) & (Group.year == 5)).all()

# print(question14)

# Задание 15. Вывести фамилии ассистентов со ставкой меньше 8000 или надбавкой меньше 800.

question15 = session.query(Teacher.last_name).filter((
    Teacher.salary < 8000) | (Teacher.premium < 800)).filter(
    Teacher.isAssistant == 1).all()

# print(question15)