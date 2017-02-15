"""Написать класс IntToStr, у которого есть одно поле: value. А тип поля - число. Его задачей должно быть реализация возможности сложения чисел и строк. Примеры:
obj = IntToStr(9.2)
print(obj + 3)  # 12.2
print('a' + obj)  # a9.2
print(obj + 'z')  # 9.2z"""

class IntToStr(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, num):
        if isinstance(num, str):
            return str(self.value) + num
        else:
            return self.value + num

    def __radd__(self, num):
        if isinstance(num, str):
            return num + str(self.value)
        else:
            return num + self.value

if __name__ == '__main__':
    obj = IntToStr(9.2)
    print(obj + 3)
    print('a' + obj)
    print(obj + 'z')