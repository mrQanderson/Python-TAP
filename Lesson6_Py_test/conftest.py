import pytest
from .company_model import *  # !!! bad import


@pytest.fixture(scope="function", autouse=True)
def create_company():
    space_company = Company('SpaceX', address='1 Rocket Road, East Hawthorne neighborhood, CA, Hawthorne, 90250, USA')
    return space_company


@pytest.fixture(scope="function", autouse=True)
def create_second_company():
    car_company = Company('Tesla', address='Tesla Road, Austin, Texas, 13101, USA')
    return car_company


@pytest.fixture(scope="function")
def create_engineer():
    jeff = Engineer("Jeff", 33)
    return jeff


def pytest_sessionstart(session):
    """Create results attributed for the session instance"""
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add test result to sessopn.results once the result is ready"""
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    """Print overall test execution status"""
    print("\nExit code:", exitstatus)
    passed = sum(1 for result in session.results.values() if result.passed)
    failed = sum(1 for result in session.results.values() if result.failed)
    print(f"Passed tests: {passed}, failed tests: {failed}")
