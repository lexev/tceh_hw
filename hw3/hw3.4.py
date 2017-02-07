
#4.Написать функцию, которая принимает
# список чисел и возвращает их произведение

def mult (lst):
    p = 1
    try:
        for i in lst:
            if isinstance(i,int) or isinstance(i, float): # Что бы умножать только числа (а не "fff"* 4, например
                p*=i
            else:
                raise (ValueError, TypeError)
        return p
    except (ValueError, TypeError):
        print('Список  должен состоять из чисел')
    return None

print(mult ([1,5,4,6,2]))
print(mult ([1,5,4,'d',2]))
