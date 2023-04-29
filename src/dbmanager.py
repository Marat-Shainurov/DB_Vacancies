import psycopg2

from src.utils import get_vacancies


class DBManager:

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        """
        Создает таблицы <employers>, <vacancies>.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    cur.execute(
                        "CREATE TABLE employers"
                        "(company_name varchar(100), company_id int PRIMARY KEY, company_link varchar(255));"

                        "CREATE TABLE vacancies"
                        "(vacancy_id int PRIMARY KEY, vacancy_name varchar, salary_from int, salary_to int, "
                        "salary_currency varchar(50),"
                        "salary_gross int,"
                        "company_id int, company_name varchar, experience varchar(50), "
                        "requirement text, responsibility text, "
                        "CONSTRAINT fk_vacancies_employers FOREIGN KEY(company_id) REFERENCES employers(company_id))"
                    )
        finally:
            connect_db_vacancies.close()

    def add_data_to_db(self):
        """
        Заполняет данными таблицы, на основе ответа API HH.ru.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    response = get_vacancies()
                    for element in response:
                        pass
        except:
            pass

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
        """

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
