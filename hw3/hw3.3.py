#3.Написать функцию, которая принимает словарь,
# преобразует все ключи словаря к строкам и возвращает новый словарь

def dicts (d):
    new_dict = {}
    for key, value in d.items():
        new_dict.update({str(key):value})
    return new_dict
print (dicts ({1: '2', 3: '4', '111': '5'}))