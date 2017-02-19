#6.2 Реализовать декоратор, который измеряет скорость выполнения функций.
#Написать три разные функции, задекорировать их и проверить
import datetime

def timer(f):
    def tmp(*args, **kwargs):
        t = datetime.datetime.now()
        res = f(*args, **kwargs)
        print ("Время выполнения функции:",  (datetime. datetime.now()-t))
        return res
    return tmp

@timer
def func(x, y):
    s = []
    for i in range(1,1000):
        s.append(x**y*i)
    return s

@timer
def func1(x, y):
    for i in range(1, 10000):
         x *=y
    return x
@timer
def func2(x, y, z):
    return x ** y ** z

func(100500, 2000)
func1(10000000, 3000)
func2(1000, 10, 6)
