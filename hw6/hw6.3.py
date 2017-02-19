#Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100

odd_gen = (item for item in range(0, 101,2))

for k in odd_gen:
    print (k)

