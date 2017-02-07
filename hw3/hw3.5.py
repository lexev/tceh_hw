#5.Написать три функции: do_work, handle_success, handle_error. do_work(my_list, success_callback, error_callback)
# принимает на вход три аргумента: список, функцию для обработки успеха и функцию для обработки ошибки.
# Ее задача проверить, что все значения в списке идут по-возрастанию.
# Если все верно: вызываем success_callback, иначе: error_callback.
# Функция handle_success пишет в консоль информацию об успешном выполнении. Функция handle_error выбрасывает ValueError


def do_work(my_list, success_callback, error_callback):
    if my_list == sorted(my_list):
        success_callback()
    else:
        error_callback()

def handle_success():
    print('Cписок отсортирован')
def handle_error():
    try:
        raise ValueError
    except ValueError as ex:
        print('Вызвано исключение {}, Список не отсортирован !'.format(ex))

#Тестирование

list0 = [1,2,3,4,5,6]
list1 = [1,2,3,4,5,5]
list2 = [1,3,7,6,7,8]
do_work(list2, handle_success, handle_error)