"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname: str, name: str, group: int, average_score: float):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __repr__(self):
        return f"<Student name = {self.name}, surname = {self.surname}, score = {self.average_score}>"

    def best_students(self, n: float):
        return list(filter(lambda st: st.average_score > n, students_list))


students_list = [
    Student('Taras', 'Java', 103135, 7.6),
    Student('Stepan', 'Python', 103136, 7.2),
    Student('Oleg', 'Script', 103155, 8.3),
    Student('Veniamin', 'Sisharp', 103155, 9.1),
    Student('Venya', 'Ruby', 103136, 5.4)
]


print(sorted(students_list))
print(sorted(students_list, reverse=True))
print(Student.best_students(students_list, 8.3))
