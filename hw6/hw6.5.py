# Написать генератор, который принимает на вход дату и на каждый вызов выдает  следующий день.

import datetime

def next_day_generator(year, month, day):
    next_day = datetime.date(year, month, day) + datetime.timedelta(days=1)
    while True:
        yield next_day
        next_day += + datetime.timedelta(days=1)

next_day = next_day_generator


for i in range(1000):
    print(next(next_day(2001,12,12))) # Тестируем от выбранной даты