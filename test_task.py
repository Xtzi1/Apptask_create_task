
# для запуска теста использовать следующую команду:
# python -m pytest -v --driver Chrome --driver-path C:/ПУТЬ ДО ПАПКИ ПРОЕКТА/Module29selenium/tests/chromedriver.exe test_task.py

import time
from selenium.webdriver.common.by import By
from data import project_to_open, email, password

def test_search_example(selenium):

    # переходим на страницу авторизации
    selenium.get('https://apptask.ru/login')

    time.sleep(2)

    # Находим поле и вводим логин
    search_input_login = selenium.find_element(By.XPATH, '//*[@id="Input_Email"]')
    search_input_login.clear()
    search_input_login.send_keys(f'{email}')

    time.sleep(2)

    # Находим поле и вводим пароль
    search_input_pass = selenium.find_element(By.XPATH, '//*[@id="password"]')
    search_input_pass.clear()
    search_input_pass.send_keys(f'{password}')

    time.sleep(5)

    # Находим кнопку и жмем поехали
    #search_button = selenium.find_element(By.XPATH,
    #                                           '//button[contains(@class, "b-button b-button--small") and text()="Поехали!"]')
    search_button = selenium.find_element(By.XPATH, '//*[@id="login"]/div[3]/button')
    search_button.click()

    time.sleep(10)

    # переходим в проект
    selenium.get(f'{project_to_open}')

    time.sleep(5)

    # переходим открываем категорию (старый локатор  '//*[@id="3"]/div[1]/span/div')
    search_button = selenium.find_element(By.XPATH, '/html/body/app/div[1]/main/div[2]/div/div[1]/div[4]/div/div/div[7]/div[1]/div[1]/span')
    search_button.click()

    time.sleep(2)

    # клик в пустое место
    search_button = selenium.find_element(By.XPATH, '//*[@id="3:1"]')
    search_button.click()

    time.sleep(2)

    # клик добавить задачу
    search_button = selenium.find_element(By.XPATH, '//*[@id="3:1"]/div')
    search_button.click()

    time.sleep(2)

    # ввод названия задачи
    search_input = selenium.find_element(By.XPATH, '//*[@id="3:1"]/div/div[2]/div[2]/div/input')
    search_input.clear()
    search_input.send_keys('Task123')

    time.sleep(2)

    # клик добавить задачу
    search_button = selenium.find_element(By.XPATH, '//*[@id="3:1"]/div/div[2]/button')
    search_button.click()

    time.sleep(2)

    #ищем айдишник задачи
    search_element_asd = selenium.find_element(By.XPATH, '//p[contains(@class, "project-card__name") and text()="Task123"]')
    search_element_number = search_element_asd.find_element(By.XPATH,
                                                            '../div[@class="project-card__footer"]/p[contains(@class, "project-card__text")]')

    text_content = search_element_number.text
    value = text_content.split(" ")[1]  # Разделить текст по пробелу и получить второй элемент

    # переходим в задачу
    selenium.get(f'https://apptask.ru/c/1376/board/1/{value}')

    time.sleep(8)

    # клик задачу в архив
    search_button = selenium.find_element(By.XPATH, '/html/body/app/div[1]/div[24]/div/div/div/div[1]/div/button[3]/span')
    search_button.click()

    time.sleep(8)

    # для запуска теста использовать следующую команду:
    # python -m pytest -v --driver Chrome --driver-path D:/PycharmProjects/Module28/Module29selenium/tests/chromedriver.exe test_task.py