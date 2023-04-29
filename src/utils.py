import json

import requests


def get_request_hh(page=0):
    """
    Делает запрос к API HH.ru, возвращает ответ в виде коллекции вакансий.
    """
    experience = ('noExperience', 'between1And3', 'between3And6', 'moreThan6')
    companies_ids = ('1455', '733', '5390761', '4130174', '3649870', '4759060', '9311920', '1740', '84585', '78638',
                     '3529', '4934')

    params = {
        'area': 113,  # индекс страны
        'page': page,  # индекс страницы
        'per_page': 100,  # максимально доступное кол-во вакансий на 1 странице
        'order_by': "salary_desc",  # встроенная сортировка по убыванию ответа по ЗП,
        'employer_id': companies_ids,
        'experience': experience,
        'only_with_salary': 'true'
    }
    req = requests.get('https://api.hh.ru/vacancies', params)

    return req.json()['items']


def get_vacancies(pages=10):
    """
    Возвращает список вакансий, на основе постраничных запросов с помощью функции get_request_hh().
    10 - максимально доступное кол-во страниц на сайте с учетом вывода 100 вакансий на страницу
    """
    response = []

    for page in range(pages):
        values = get_request_hh(page)
        response.extend(values)

    return response


def add_data_to_file(data):
    """
    Вспомогательная временная функция для записи ответа API в файл.
    """
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

add_data_to_file(get_vacancies())