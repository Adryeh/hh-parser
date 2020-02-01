import random
import requests
from bs4 import BeautifulSoup
from collections import namedtuple
from utils import user_agents_list


USER_QUERY = "Python junior"
BASE_URL = "https://hh.ru"
URL = f"https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=" \
      f"true&enable_snippets=true&text={'+'.join(USER_QUERY.split())}&page=0"


Vacancy = namedtuple("Vacancy", "title company metro link salary")


def get_html(url, user_agent):
    # запрос на источник
    response = requests.get(url, headers={'User-Agent': user_agent})
    return response


def parse_data():
    baser_url = BASE_URL
    url = URL
    data = []
    while True:
        user_agent = str(random.choice(user_agents_list))
        html = get_html(url, user_agent).text
        soup = BeautifulSoup(html, "lxml")
        soup.prettify(formatter=lambda s: s.replace(u'\xa0', ' '))
        # Находим все блоки вакансий
        vacancies = soup.find_all("div", {"class": "vacancy-serp-item"})
        # Получаем нужные данные по каждому блоку
        for vacancy in vacancies:
            try:
                title = vacancy.find("div", {"class": "resume-search-item__name"}).text
            except:
                title = 'No title'
            try:
                link = vacancy.find("a")['href']
            except:
                link = 'No link'
            try:
                company = vacancy.find("a", {"class": "bloko-link_secondary"}).text
            except:
                company = 'No company'
            try:
                metro = vacancy.find("span", {"class": "vacancy-serp-item__meta-info"}).text
            except:
                metro = 'No metro'
            try:
                salary = vacancy.find("div", {"class": "vacancy-serp-item__compensation"}).text.replace(u'\xa0', u' ')
            except:
                salary = 'No salary'
            # Объеденяем данные в namedtuple Vacancy
            item_data = Vacancy(title, company, metro, link, salary)
            data.append(item_data)

        next_button = soup.find('a', class_='HH-Pager-Controls-Next', href=True)

        if next_button:
            url = baser_url + next_button['href']
        else:
            break
    return data
