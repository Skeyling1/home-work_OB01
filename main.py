#Менеджер задач
#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task():
    def __int__(self, description, dead_line, state):
        self.description = description
        self.dead_line = dead_line
        self.state = state

    def add_task(self):
        task = input("введите задачу")


    def done_mark(self):
        pass

    def do_list(self):
        print()