import requests
import psycopg2
import os

# func1 from utils requests data
# method adds data to the DB
# class operates with the data via connect()

class DBManager:

    def __int__(self, db_name):
        self.db_name = 'DB_Vacancies'

    def add_data_to_db(self):

        connect_db_vacancies = psycopg2.connect(
            host='localhost', database=self.db_name, user='postgres', password='Benzokolon1')

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
