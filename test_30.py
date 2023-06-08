import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True, scope='function')
def testing():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        executable_path = './chromedriver.exe'
        service = Service(executable_path=executable_path)
        pytest.driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Ошибка инициализации WebDriver: {e}")
        return

    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    pytest.driver.find_element(By.ID, 'pass').send_keys('12345')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


   #python -m pytest -v --driver Chrome --driver-path D:/PycharmProjects/Module28/Module29selenium/tests/chromedriver.exe test_30.py