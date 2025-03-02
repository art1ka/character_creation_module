import datetime as dt
import time


class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time:
            return 'С этим испытанием вы уже справились.'
        self.start_time = dt.datetime.now()
        return f'Начало квеста "{self.name}" положено.'

    def pass_quest(self):
        if not self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен.'
                f' Время выполнения квеста: {completion_time}')

    # Напишите код метода __str__.
    def __str__(self):
        if self.end_time is not None:
            return (f'Цель квеста {self.name} — {self.goal}. Квест завершён.')
        elif self.start_time is not None:
            return ('Цель квеста {название_квеста} — '
                    '{цель_квеста}. Квест выполняется.')
        else:
            return (f'Цель квеста {self.name} — {self.goal}.')


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal)

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

# Печатаем объекта класса Quest:
print(new_quest)
