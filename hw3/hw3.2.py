#2.Написать функцию, которая принимает на вход список, если в списке все объекты - int,
# сортирует его. Иначе выбрасывает ValueError
def sort_int_list(lst):
    srtlist = []
    try:
        for i in lst:
            if not isinstance(i, int):
                raise ValueError()
        srtlist  = sorted(lst)
        print('Отсортированный список', srtlist)

    except ValueError:
        print(' Не все элемент списка типа int')


sort_int_list([1, 3, 4, 5, 12, 11])
sort_int_list(['String', 1, 3, 4, 5, 12, 11])