# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.


class Task:
    def __init__(self, description, dead_line, accomp):
        self.description = description
        self.dead_line = dead_line
        self.accomp = accomp

    def add_task(self):
        self.description = input("введите задачу: ")
        self.dead_line = input("введите срок выполнения: ")
        self.accomp = False

    def done_mark(self):
        self.accomp = True

tasks = []

while True:
    print("текущие задачи:")
    if tasks:
        s = 1
        for i in tasks:
            if i.accomp != True:
                print("задача №", s, ":  ", i.description, "\t", end="")
                print("закончить до:  ", i.dead_line)
                s += 1
    else: print("нет задач")



    print("\nвведите 0 для добавления задачи ")
    print("введите 1 для отметки о выполнении ")
    print("введите 2 для просмотра актуальных задач ")
    print("нажмите любую другую кнопку для выхода ")
    comand = input()
    if comand == "0":
        a = Task(True, True, True)
        a.add_task()
        tasks.append(a)


    elif comand == "1":
        pass
    elif comand == "2":
        s = 1
        for i in tasks:
            if i.accomp != True:
                print("задача №", s, ":  ", i.description, "\t", end="")
                print("закончить до:  ", i.dead_line)
                s += 1



    else: break



