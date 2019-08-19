# 2. Создать пользовательский класс данных (или использовать) один из классов,
# реализованных в курсе Python.Основы. Реализовать класс с применением слотов
# и обычным способом. Для объекта обычного класса проверить отображение словаря
# атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих


from memory_profiler import profile
from pympler import asizeof


class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_fullname(self):
        fullname = self.name + ' ' + self.patronymic + ' ' + self.surname
        return fullname


class PersonSlots:
    __slots__ = ('name', 'surname', 'patronymic')

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_fullname(self):
        fullname = self.name + ' ' + self.patronymic + ' ' + self.surname
        return fullname


person = Person('Max', 'Shokurov', 'Artyomovich')
person_slots = PersonSlots('Max', 'Shokurov', 'Artyomovich')


@profile
def per():
    print(f'Links: {asizeof.asizeof(person)}')

@profile
def per_slots():
    print(f'Links: {asizeof.asizeof(person_slots)}')


per()
per_slots()


# Links: 528
# Filename: C:/Users/shoku/PycharmProjects/algorithms/Homework_6/homework_6_task_2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     39     17.0 MiB     17.0 MiB   @profile
#     40                             def per():
#     41     17.0 MiB      0.0 MiB       print(f'Links: {asizeof.asizeof(person)}')
#
#
# Links: 248
# Filename: C:/Users/shoku/PycharmProjects/algorithms/Homework_6/homework_6_task_2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     43     17.0 MiB     17.0 MiB   @profile
#     44                             def per_slots():
#     45     17.0 MiB      0.0 MiB       print(f'Links: {asizeof.asizeof(person_slots)}')
#
# Видно, что при работе со слотами кол-во ссылок на переменные более чем в два раза меньше, кол-во исползуемой памяти
# одинаково.