from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testSelenium.base import Base


class TestTime(Base):
    def test_wait(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹")
        self.driver.find_element_by_id("su").click()
        # 在Web自动化测试中，特别是在使用Selenium库时，expected_conditions
        # 这些方法通常需要一个定位器（locator）作为参数，而定位器是一个元组，包含定位方法和选择器。正确的做法是将定位器和选择器作为一个整体传递，即使用圆括号将它们括起来，形成一个元组
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="s_tab"]')))
        self.driver.find_element_by_xpath('//*[@id="s_tab"]//a[1]').click()

