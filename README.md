# DB_Vacancies
#
# Цель проекта
# Проект создан для получения актуальной информации о вакансия в выбранных компаниях, 
# на основе данных, полученных от API HH.ru
#
# Структура проекта
# Все необходимые зависимости указаны в requirements.
# pacakge 'src' - основной пакет проекта.
# - utils.py - содержит 2 функции для запроса к API (get_request_hh), 
#   и для формирования необходимого списка вакансий для дальнейшего использования (get_vacancies).
# - db.manager.py - содержит класс DBManager, для работы с базой данных.
# - queries.sql - содержит копии команд SQL, использованных в проекте.
# - tables_template.xlsx - шаблон таблиц, созданный при планировании контента DB.
# - package tests использован для тестирования функций из utils.py. 
#   Все методы DBManager проверялись непосредственно в pgadmin.
#
# Подбор 10 компаний для поиска.
# companies_names = ['HeadHunter', 'ЛАНИТ', 'Совкомбанк технологии', 'Runexis', 'Right Line',
# 'HR Prime', 'DNS Технологии', 'Яндекс', 'Авито', 'Тинькофф', 'Сбер', 'Билайн'].
# Соответствующие company_id для запроса к API HH.ru
# companies_ids = ['1455', '733', '5390761', '4130174', '3649870', '4759060', '9311920', '1740', '84585', '78638', '3529', '4934']
# Компании выбраны на основе следующих статей: 
# https://habr.com/ru/specials/647609/, 
# https://habr.com/ru/specials/539624/,
# https://atlasnews.ru/rejting-top-10-it-kompanij-rossii/
#
# Работа с проектом
# Для работы с проектом необходимо:
# # - В файле main.py указать для инициализируемого экземпляра класса название созданной DB и Ваш пароль.
# - После - запустить файл main.py.
#   - Будет создана БД.
#   - Будет создан экземпляр класса (строка db_object = DBManager('Your DB name', 'Your password'))
#   - Будут созданы таблицы в базе данных (строка db_object.create_tables()).
#   - Будет заполнены таблицы в базе данных (строка db_object.add_data_to_db_vacancies()).
# - Далее необходимо снять комментарий с необходимого метода в файле main.py, 
#   закомментировав вызов методов create_db(), create_tables() и add_data_to_db_vacancies() (строки 5-8)