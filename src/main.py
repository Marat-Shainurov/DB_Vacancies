from src.dbmanager import DBManager
from config import config


def main():
    # Создание объекта парсера, экземпляра класса DBManager, создание базы данных и таблиц.
    # Необходимо указать необходимое название базы данных.
    params = config()
    db_object = DBManager('your_db_name', params)
    db_object.create_db()
    db_object.create_tables()

    # Заполнение таблиц на основе запроса к API HH.ru.
    db_object.add_data_to_db_vacancies()

    # Получение списка всех компаний и количество вакансий у каждой компании
    db_object.get_companies_and_vacancies_count()

    # Получение списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    db_object.get_all_vacancies()

    # Получение списка всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
    db_object.get_vacancies_with_keyword('python')

    # Получение средней зарплаты по вакансиям.
    print('Средняя ЗП -', db_object.get_avg_salary(), 'RUR')

    # Получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
    db_object.get_vacancies_with_higher_salary()


if __name__ == '__main__':
    main()
