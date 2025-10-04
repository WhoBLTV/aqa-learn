import pytest


@pytest.fixture(scope="function")
def browser_settings():
    print("Браузер!")

    yield

    print("Закрываем браузер!")