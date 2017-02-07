#Реализовать класс Person, у которого должно быть два публичных поля: age и name. Также у него должен быть
# следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых.
#  И метод is_known(person), который возвращает, знакомы ли два человека
class Person(object):

    def __init__(self, age, name, list_know = []):
        self.age = age
        self.name = name
        self.list_know = list_know

    def known(self, person):
        self.list_know.append(person.name) #Если Пете мы добавляем в знакомые Васю,
        person.list_know.append(self.name) #то в знакомые Васи мы должны добавить и Петю
        print('{} теперь знаком с {}'.format(self.name, person.name))

    def is_known(self, person):
        if person.name in self.list_know and self.name in person.list_know: #Если Петя в знакомых у Васи, то его Петя тоже знает Васю
            print('{} знаком с  {}'.format(self.name, person.name))
        else:
            print(' {} не знает  {}'.format(self.name, person.name))


person1 = Person(30, 'Петя')
person2 = Person(40, 'Вася')
person3 = Person(35, 'Ваня')
person4 = Person(43, 'Рома')

person1.known(person2)
person1.known(person3)
person1.is_known(person2)
person2.is_known(person3)
person2.is_known(person1)
person2.is_known(person4) #Вася не знает Рому

