"""Для задания Company model, замените check_yourself на несколько независимых юнит-тестов, используя при этом Pytest.

Примечания:
•	обязательно использование хотя бы одной фикстуры
•	обязательно использование хотя бы одного пайтест хука
•	обязательно использование хотя бы одной пайтест метки
•	используйте pytest --html=report.html --self-contained-html плагин для создания HTML репорта
•	используйте pytest-xdist плагин для параллельного запуска тестов
•	параметры для плагинов должны быть заданы в pytest.ini
"""
import pytest


@pytest.mark.smoke
def test_employees_join_company(create_company, create_engineer):
    assert not create_engineer.is_employed
    create_engineer.join_company(create_company)
    assert create_engineer.is_employed
    assert create_engineer.company.name == "SpaceX"


@pytest.mark.smoke
def test_engineer_makes_money(create_company, create_engineer):
    create_engineer.join_company(create_company)
    assert not create_engineer._money
    create_engineer.do_work()
    assert create_engineer._money == 10


def test_engineer_change_company(create_engineer, create_company, create_second_company):
    create_engineer.join_company(create_company)
    create_engineer.become_unemployed()
    assert not create_engineer.is_employed
    create_engineer.join_company(create_second_company)
    assert create_engineer.company.name == "Tesla"


@pytest.mark.skip(reason="Marking example")
def test_get_error_if_employee_join_two_companies(create_engineer, create_company, create_second_company):
    with pytest.raises(AttributeError) as error:
        create_engineer.join_company(create_company)
        create_engineer.join_company(create_second_company)
    assert str(error.value) == "Jeff is already employed"


def test_get_error_if_employee_work_and_not_employed(create_engineer):
    with pytest.raises(AttributeError) as error:
        create_engineer.do_work()
    assert str(error.value) == "Jeff is not employed to have a work"
