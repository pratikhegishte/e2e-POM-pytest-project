import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import config
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def driver():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()
    # driver.get(config.URL)
    # yield driver
    # driver.quit()
    options = Options()      # code for the headless browser
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(config.URL)
    yield driver
    driver.quit()