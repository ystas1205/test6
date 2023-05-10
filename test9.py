class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        grade = []
        for value in self.grades.values():
            grade.append(sum(value))
            self.average_student_assessment = (sum(grade) / (len(self.grades) * 2))
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_student_assessment} \nКурсы в процессе изучения:{', '.join(self.courses_in_progress)}\nЗавершенные курсы:{''.join(self.finished_courses)}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_student_assessment < other.average_student_assessment


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        grade = []
        for value in self.grades.values():
            grade.append(sum(value))
            self.average_lecturer_assessment = (sum(grade) / (len(self.grades) * 2))
            return f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции: {self.average_lecturer_assessment}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_lecturer_assessment < other.average_lecturer_assessment


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_student_course_grade(list_student, course):
    grade = []
    for value in list_student:
        grade.append(sum(value[course]))
    print(f'Средняя оценка cтудентов курса {course} = {sum(grade) / (len(grade) * 2)}')


def average_course_grade_lecturers(list_lecturer, course):
    grade = []
    for value in list_lecturer:
        grade.append(sum(value[course]))
    print(f'Средняя оценка лекторов курса {course} = {sum(grade) / (len(grade) * 2)}')


some_student = Student('Makarov', 'Misha', 'your_gender')
some_student2 = Student('Maksimov', 'Аleksandr', 'men')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += [' Введение в программирование']
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += [' Введение в программирование']

some_reviewer = Reviewer('Ivanov', 'ivan')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 5)
some_reviewer.rate_hw(some_student, 'Git', 1)
some_reviewer.rate_hw(some_student, 'Git', 4)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 7)
some_reviewer.rate_hw(some_student2, 'Git', 3)
some_reviewer.rate_hw(some_student2, 'Git', 5)

some_lecturer = Lecturer('Petrov', 'Misha')
some_lecturer2 = Lecturer('Savin', 'Sergey')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Git']

some_student.rate_lecturer(some_lecturer, 'Python', 5)
some_student.rate_lecturer(some_lecturer, 'Python', 3)
some_student.rate_lecturer(some_lecturer, 'Git', 2)
some_student.rate_lecturer(some_lecturer, 'Git', 5)
some_student2.rate_lecturer(some_lecturer2, 'Python', 5)
some_student2.rate_lecturer(some_lecturer2, 'Python', 1)
some_student2.rate_lecturer(some_lecturer2, 'Git', 8)
some_student2.rate_lecturer(some_lecturer2, 'Git', 4)

print(some_reviewer)
print()
print()
print()
print(some_lecturer)
print(some_lecturer.grades)
print()
print(some_lecturer2)
print(some_lecturer2.grades)
print()
print()
print()
print(some_student)
print(some_student.grades)
print()
print(some_student2)
print(some_student2.grades)
print()
print()
print()
average_student_course_grade([some_student.grades, some_student2.grades], 'Python')
average_course_grade_lecturers([some_lecturer.grades, some_lecturer2.grades], 'Git')
print()
print()
print(some_student < some_student2)
print()
print()
print(some_lecturer < some_lecturer2)
