#1.Написать функцию, которая выбрасывает одно из трех исключений:
# ValueError, TypeError или RuntimeError случайным образом. В месте вызова функции обрабатывать все три исключения

def three_exept():
    import random
    list_of_except = [ValueError('ValueError'), TypeError("TypeError"), RuntimeError('RuntimeError')]
    r = random.choice (list_of_except)
   # print(r)
    raise r

# Согласно условию, обрабатваем исключение в МЕСТЕ ВЫЗОВА функии
try:
    three_exept()
except (ValueError, TypeError, RuntimeError) as ex:
    print('Вызвано исключение {} !'.format(er))
