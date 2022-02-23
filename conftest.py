from datetime import datetime
import psycopg2
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def postgres_connections():
    db = psycopg2.connect(dbname='postgres', user='postgres',
                          password='postgres', host='localhost')
    yield db
    db.close()
