"""Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы на другие."""
import requests, re


def get_links(url):
    response = requests.get(url)

    list_links = re.findall('a href=\"(https?://.+?)"', str(response.content), flags=re.MULTILINE)
    for link in list_links:
        print(link)



if __name__ == '__main__':
    get_links('https://habrahabr.ru/')