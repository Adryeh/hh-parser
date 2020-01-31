import requests
from bs4 import BeautifulSoup
from collections import namedtuple


BASE_URL = "https://hh.ru"
URL = "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=" \
      "true&enable_snippets=true&text=Python+junior&page=0"


Vacancy = namedtuple("Vacancy", "title company metro link")


def get_html(url):
    # запрос на источник
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return response


def parse_data():
    baser_url = BASE_URL
    url = URL
    data = []
    while True:
        html = get_html(url).text
        soup = BeautifulSoup(html, "lxml")
        # Находим все блоки вакансий
        vacancies = soup.find_all("div", {"class": "vacancy-serp-item"})
        # Получаем нужные данные по каждому блоку
        for vacancy in vacancies:
            title = vacancy.find("div", {"class": "resume-search-item__name"}).text
            link = vacancy.find("a")['href']
            company = vacancy.find("a", {"class": "bloko-link_secondary"}).text
            metro = vacancy.find("span", {"class": "vacancy-serp-item__meta-info"}).text
            # Объеденяем данные в namedtuple Vacancy
            item_data = Vacancy(title, company, metro, link)
            data.append(item_data)

        next_button = soup.find('a', class_='HH-Pager-Controls-Next', href=True)

        if next_button:
            url = baser_url + next_button['href']
        else:
            break
    return data

