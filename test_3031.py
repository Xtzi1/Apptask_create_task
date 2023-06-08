import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True, scope='function')
def testing():
    try:
        driver_path = './chromedriver.exe'
        service = Service(driver_path)
        pytest.driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Ошибка инициализации WebDriver: {e}")
        return

    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    # Авторизация
    email = pytest.driver.find_element(By.CSS_SELECTOR, 'input#email')
    password = pytest.driver.find_element(By.CSS_SELECTOR, 'input#pass')
    submit_button = pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    email.send_keys('a@a.a')
    password.send_keys('123456')
    submit_button.click()

    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')

    yield

    pytest.driver.quit()


def test_all_pets_present():

    # Явное ожидание таблицы с питомцами
    pet_list = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    pets = pytest.driver.find_elements(By.XPATH, "//table/tbody/tr")

    table = pet_list.find_element(By.CSS_SELECTOR, 'table.table.table-hover')
    rows = table.find_elements(By.CSS_SELECTOR, 'tbody tr')

    names = [pet.find_element(By.XPATH, "./td[1]").text for pet in pets]
    pet_count = len(names)

    # Инициализируем счетчик
    count = 0
    # Цикл для подсчета элементов
    for row in rows:
        count += 1
    assert count == pet_count, f"Количество питомцев на странице ({len(pets)}) меньше общего количества ({pet_count})"


def test_half_pets_have_photos():
    # Явное ожидание таблицы с питомцами
    pet_list = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    pets = pet_list.find_elements(By.XPATH, "//table/tbody/tr")
    names = [pet.find_element(By.XPATH, "./td[1]").text for pet in pets]
    pet_count = len(names)

    photo_count = 0
    # Инициализируем счетчик
    for pet in pets:
        img_element = pet.find_element(By.XPATH, ".//th/img")
        src = img_element.get_attribute("src")
        if src:  # Проверяем, что атрибут src не пустой
            photo_count += 1

    assert photo_count >= pet_count / 2, f"Количество питомцев с фото ({photo_count}) меньше половины общего количества ({pet_count / 2})"


def test_all_pets_have_details2():
    # Явное ожидание таблицы с питомцами
    pet_list = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    # Установка неявного ожидания веб-драйвера
    pytest.driver.implicitly_wait(5)

    pets = pet_list.find_elements(By.XPATH, "//table/tbody/tr")
    for pet in pets:
        name = pet.find_element(By.XPATH, "./td[1]").text
        age = pet.find_element(By.XPATH, "./td[3]").text
        breed = pet.find_element(By.XPATH, "./td[2]").text
        assert name, f"У питомца отсутствует имя: {pet.text}"
        assert age, f"У питомца отсутствует возраст: {pet.text}"
        assert breed, f"У питомца отсутствует порода: {pet.text}"


def test_all_pets_have_unique_names():
    # Явное ожидание таблицы с питомцами
    pet_list = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    pets = pet_list.find_elements(By.XPATH, "//table/tbody/tr")
    names = [pet.find_element(By.XPATH, "./td[1]").text for pet in pets]
    assert len(names) == len(set(names)), "У некоторых питомцев обнаружены одинаковые имена"


#python -m pytest -v --driver Chrome --driver-path D:/PycharmProjects/Module28/Module29selenium/tests/chromedriver.exe test_3031.py


