# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод: log(*values).
# Написать класс FormattedPrinter,
# который выводит в консоль информацию, окружая ее строками из *

#Родитель выводит список
class Printer:
    def log(self,*args):
        for k in self.args:
            print(k, end=' ')


class FormattedPrinter(Printer): # Наследник Printer обрамляет список звездочками
   def __init__(self, *args): #Вывод для простоты будем осуществлять в конструкторе
       self.args = args
       print('*' * 100)
       super().log(self, *args) #Вызываем метод объекта-родителя
       print('\n')
       print('*' * 100)


a = FormattedPrinter(1, 2, 3, 4, 'dfg')
