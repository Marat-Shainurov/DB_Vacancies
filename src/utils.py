import json

import requests


def get_request_hh(page=0):
    """
    Делает запрос к API HH.ru, возвращает ответ в виде коллекции вакансий.
    """

    companies_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    params = {
        'area': 113,  # индекс страны
        'page': page,  # индекс страницы
        'per_page': 100,  # максимально доступное кол-во вакансий на 1 странице
        'order_by': "salary_desc",  # встроенная сортировка по убыванию ответа по ЗП,
        'employer_id': '1455'
        # 'search_field': 'employer',
        # 'text': 'Яндекс'
    }
    req = requests.get('https://api.hh.ru/vacancies', params)

    return req.json()['items']


def get_vacancies():
    """
    Возвращает список вакансий, на основе постраничных запросов с помощью функции get_request_hh().
    10 - максимально доступное кол-во страниц на сайте с учетом вывода 100 вакансий на страницу
    """
    pages = 10
    response = []

    for page in range(pages):
        values = get_request_hh(page)
        response.extend(values)

    return response


def get_request_employers(page=0):
    """
    Вспомогательный метод для получения списка работодателей.
    """
    params = {
        'area': 113,  # индекс страны
        'page': page,  # индекс страницы
        'per_page': 100,  # максимально доступное кол-во вакансий на 1 странице
    }
    req = requests.get('https://api.hh.ru/employers', params)

    return req.json()

#
# def get_employers():
#     pages = 10
#     response = []
#
#     for page in range(pages):
#         values = get_request_employers(page)
#         response.extend(values)
#
#     return response
#
#
# def add_employers_to_file(data):
#     with open('employers.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#
#
# def add_salary_sorting():
#     """Добавляет атрибут с ЗП, рассчитанной в едином подходе, для дальнейших расчетов и сортировок"""
#
