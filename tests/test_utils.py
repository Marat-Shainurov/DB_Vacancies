from src.utils import get_request_hh, get_vacancies


def test_get_request_hh():
    response = get_request_hh()
    assert len(response) == 100


def test_get_vacancies():
    response = get_vacancies(2)
    assert len(response) == 200
