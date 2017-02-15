class Stack(object):

    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.list == []:
            raise IndexError('Стек пуст!')
        else:
            return self.list.pop(len(self.list) - 1) # возвращаем верхний элемент стека и удаляем его из стека

# проверка
stack1 = Stack()
stack1.push('stroka')
stack1.push( '2222')
stack1.push(444)
stack1.push('1111111')
stack1.push('qwweer')
print(stack1.list)
print (stack1.pop())

print(stack1.list)
print ('Теперь тестируем пустой стек')
st = Stack()
print(st.list)
st.pop() # Пробуем извлеь из пустого стека
print(st.list)