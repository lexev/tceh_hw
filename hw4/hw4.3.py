#Написать класс Animal и Human, сделать так,
#чтобы некоторые животные были опасны для человека (хищники, ядовитые).
#Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Human(object):
    def is_dangerous(self, animal):
        if animal.danger:
            print('Животное опасно')
        else:
            print('Животное не опасно')

class Animal(object):
    def __init__(self, danger):
        self.danger = danger


fish = Animal(False)
cat = Animal(False)
tiger = Animal(True)
h = Human()
h.is_dangerous(fish) #Рыба не опасна
h.is_dangerous(cat)  #Кошка не опасна
h.is_dangerous(tiger) #Тигр опасен