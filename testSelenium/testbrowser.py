import os

from selenium import webdriver


def setup():
    browser = os.getenv("browser")
    if browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'headless':
        driver = webdriver.PhantomJS()

    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()