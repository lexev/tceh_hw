# 6.1 Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана

def deco_cancel_run_function (func):
    def cancel(*args):
        print ('Функция {} не будет вызвана'.format (func.__name__))
        return None
    return  cancel
# Тестирование без декоратора
def function (*args):
    print (args)

function (1,2,4,5,7) #выводит аргументы

print('Тестирование с декоратором')
@deco_cancel_run_function
def function (*args):
    print (args)


function (1,2,4,5,7)#не выводит аргументы
