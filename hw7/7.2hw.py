"""Реализовать следующую логику: получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/,
# выводить в консоль все пары "ключ-значение", сохранять полученный json в файл."""
import json, requests

r = requests.get('https://jsonplaceholder.typicode.com/')
for k, v in r.headers.items():
    print(k, ' - ', v)
with open('output.txt', 'w') as f:
    f.write(json.dumps(dict(r.headers)))
    f.close()
