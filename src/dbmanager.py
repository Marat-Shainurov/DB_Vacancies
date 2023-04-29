import psycopg2

from src.utils import get_vacancies


class DBManager:

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        """
        Создает таблицы <employers>, <vacancies>.
        Заполняет таблицу <employers> с названиями выбранных компаний и их company_id.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    cur.execute(
                        "CREATE TABLE employers"
                        "(company_name varchar(100), company_id int PRIMARY KEY);"

                        "INSERT INTO employers "
                        "(company_name, company_id) VALUES"
                        "('HeadHunter', '1455'), ('ЛАНИТ', '733'), ('Совкомбанк технологии', '5390761'),"
                        "('Runexis', '4130174'), ('Right Line', '3649870'), ('HR Prime', '4759060'),"
                        "('DNS Технологии', '9311920'), ('Яндекс', '1740'), ('Авито', '84585'),"
                        "('Тинькофф', '78638'), ('Сбер', '3529'), ('Билайн', '4934');"

                        "CREATE TABLE vacancies"
                        "(vacancy_id int PRIMARY KEY, vacancy_name varchar, salary_from int, salary_to int, "
                        "salary_currency varchar(50), vacancy_link varchar,"
                        "company_id int, company_name varchar, company_link varchar, experience varchar(50), "
                        "requirement text, responsibility text,"
                        "CONSTRAINT fk_vacancies_employers FOREIGN KEY(company_id) REFERENCES employers(company_id));"
                    )
        finally:
            connect_db_vacancies.close()

    def add_data_to_db_vacancies(self):
        """
        Заполняет данными таблицу vacancies, на основе ответа API HH.ru.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    response = get_vacancies()
                    for element in response:
                        cur.execute(
                            "INSERT INTO vacancies (vacancy_id, vacancy_name, salary_from, salary_to, salary_currency, "
                            "vacancy_link, company_name, company_id, company_link, experience, requirement, "
                            "responsibility) "
                            "Values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (element['id'], element['name'], element['salary']['from'], element['salary']['to'],
                             element['salary']['currency'], element['alternate_url'],
                             element['employer']['name'], element['employer']['id'],
                             element['employer']['alternate_url'], element['experience']['id'],
                             element['snippet']['requirement'], element['snippet']['responsibility'])
                        )
        finally:
            connect_db_vacancies.close()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    cur.execute(
                        "SELECT company_name, COUNT(*) as vacancy_numbers "
                        "FROM vacancies "
                        "GROUP BY company_name "
                        "ORDER BY vacancy_numbers DESC"
                    )
                    rows = cur.fetchall()
                    for row in rows:
                        print(f'{row[0]} --- {row[1]} вакансий.')
                        print('-' * 30)
        finally:
            connect_db_vacancies.close()

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

        try:
            with connect_db_vacancies:
                with connect_db_vacancies.cursor() as cur:
                    cur.execute(
                        "SELECT company_name, vacancy_name, salary_to, salary_from, salary_currency, vacancy_link "
                        "FROM vacancies")
                    rows = cur.fetchall()
                    for row in rows:
                        # print(f'{row[0]} - {row[1]} вакансий.')
                        print(f'{row[0]} --- {row[1]} --- От {row[2]} до {row[3]} {row[4]} --- Ссылка {row[5]}')
                        print('-' * 130)
        finally:
            connect_db_vacancies.close()

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
