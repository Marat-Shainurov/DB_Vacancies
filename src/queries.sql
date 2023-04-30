-- Создание базы данных.
CREATE DATABASE 'Your_DB_name'"

-- Создание таблиц employers и vacancies.
CREATE TABLE employers
(
	company_name varchar(100),
	company_id int PRIMARY KEY
);

INSERT INTO employers (company_name, company_id) VALUES
('HeadHunter', '1455'), ('ЛАНИТ', '733'), ('Совкомбанк технологии', '5390761'),
('Runexis', '4130174'), ('Right Line', '3649870'), ('HR Prime', '4759060'),
('DNS Технологии', '9311920'), ('Яндекс', '1740'), ('Авито', '84585'),
('Тинькофф', '78638'), ('Сбер', '3529'), ('Билайн', '4934');

CREATE TABLE vacancies
(
	vacancy_id int PRIMARY KEY,
	vacancy_name varchar,
	salary_from int,
	salary_to int,
	salary_currency varchar(50),
	vacancy_link varchar,
	company_id int,
	company_name varchar,
	company_link varchar,
	experience varchar(50),
	requirement text,
	responsibility text,

	CONSTRAINT fk_vacancies_employers FOREIGN KEY(company_id) REFERENCES employers(company_id)
);

-- Получает список всех компаний и количество вакансий у каждой компании
-- (для метода get_companies_and_vacancies_count)
SELECT company_name, COUNT(*) as vacancy_numbers
FROM vacancies
GROUP BY company_name
ORDER BY vacancy_numbers DESC;

-- Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
--- (для метода get_all_vacancies)
SELECT company_name, vacancy_name, salary_to, salary_from, salary_currency, vacancy_link
FROM vacancies;

-- Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
-- (для метода get_vacancies_with_keyword)
SELECT company_name, vacancy_name, salary_to, salary_from, salary_currency, vacancy_link
FROM vacancies
WHERE LOWER(vacancy_name) LIKE LOWER('%python%')

-- Получает среднюю зарплату по вакансиям.
-- (для метода get_avg_salary)
SELECT SUM(CASE
WHEN salary_from IS NULL THEN (salary_to * 0.7)
WHEN salary_currency != 'RUR' THEN salary_from * 80 ELSE salary_from END) / COUNT(*) as average_salary
FROM vacancies


-- Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
-- (для метода get_vacancies_with_higher_salary)
-- Для примера использована произвольная цифра 100000, как средняя. Метод использует метод get_avg_salary для расчета.
SELECT company_name, vacancy_name, salary_to, salary_from, salary_currency, vacancy_link,
CASE
WHEN salary_from IS NULL THEN (salary_to * 0.7)
WHEN salary_currency != 'RUR' THEN salary_from * 80 ELSE salary_from END as salary_to_compare
FROM vacancies
WHERE (CASE WHEN salary_from IS NULL THEN (salary_to * 0.7)
WHEN salary_currency != 'RUR' THEN salary_from * 80 ELSE salary_from END) >= 100000