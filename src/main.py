from src.dbmanager import DBManager

# get_request_hh() and get_vacancies() from utils request data from HH api
# a DBManager class object is created
# add_data_to_db() method adds data to the DB
# class methods operate with the data


obj = DBManager('DB_Vacancies')
# obj.create_tables()
# obj.add_data_to_db_vacancies()
obj.get_companies_and_vacancies_count()
# obj.get_all_vacancies()
