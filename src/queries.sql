
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
	company_id int,
	company_name varchar,
	company_link varchar,
	experience varchar(50),
	requirement text,
	responsibility text,

	CONSTRAINT fk_vacancies_employers FOREIGN KEY(company_id) REFERENCES employers(company_id)
);
