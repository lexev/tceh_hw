""" Написать списковые выражения, которые:
создают список из строк всех нечетных чисел от 1 до 100
создают список из объектов другого списка, кроме итерируемых
создают список из фразы 'The quick brown fox jumps over the lazy dog', где каждый объект списка - кортеж из:
слова в верхнем регистре, слова в случайном регистре (qUIcK) и длины слова"""

lst = [str (x) for x in range(1,100,2)] #1 вариант
lst1 = [str (x) for x in range(1,100) if x % 2 != 0] #2 вариант
lst2 = [str (x) for x in range(100) if x % 2 != 0] #1 вариант
print (lst, end = '\n')
print (lst1, end = '\n')
print (lst2)

list_with_iter = [1,3,(1,4,5,), ['q','w','r'], 'asd',[1,3], 'qwerty',2,'d']

list_without_iter = [item for item in list_with_iter if not hasattr(item,'__iter__')]
print (list_without_iter)

string = 'The quick brown fox jumps over the lazy dog'
from random import choice
three_tuples_list = [(word.upper(), ''.join([choice([letter.upper(), letter.lower()]) for letter in word]), len(word)) for word in string.split()]

print(three_tuples_list)