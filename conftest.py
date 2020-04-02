import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser_is_opened():
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')
    chrome_opt.add_argument('--no-sandbox')
    driver = webdriver.Chrome('./chromedriver', options=chrome_opt)
    # driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.close()
