"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n
- метод generate, который принимает длину последовательности n
- метод print_seq, который выводит последовательность на экран
"""


class RandSequence:
    sequence = []
    n: int = 0

    def __init__(self, n):
        self.n = n

    def generate(self, n):
        self.sequence = [i for i in range(n)]

    def print_seq(self):
        return self.sequence
