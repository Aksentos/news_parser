import requests
from bs4 import BeautifulSoup as bs

# сначала устанавливаем нужные библиотеки

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/39.0.2171.95 Safari/537.36"
}
# список адресов, откуда хотим брать новости
URLS = ["https://op-ex.ru/post_news/", 'https://op-ex.ru/post_news/page/2/']


# собираем инфу с сайта
def get_data(url):
    try:
        page = requests.get(url, headers=HEADERS)
    except Exception as e:
        return f"Ошибка ввода URL-адреса. {e}"

    # собираем весь html код страницы
    soup = bs(page.text, "lxml")

    # собираем все что нам нужно
    data = soup.find_all('div', class_='col-12 mb-4')
    return data


# Отфильтровываем нужные нам данные и записываем в файл (этот фильтр подойдет только для news.mail.ru)
def add_to_file(data):
    with open("news.txt", "a", encoding="utf-8") as file:
        for item in data:
            title = item.find('a', class_='text-body stretched-link').text # заголовок новости
            url = item.find('a', class_='text-body stretched-link').get("href")  # ссылка на статью
            file.write(f"{title}. Ссылка: {url}\n")  # сохраняем запись в файл


if __name__ == "__main__":
    for url in URLS:
        add_to_file(get_data(url))


