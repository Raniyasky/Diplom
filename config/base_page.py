from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        """Открывает страницу по URL"""
        self.driver.get(url)

    def wait_for_element(self, by: By, value: str, timeout: int = 10):
        """Ожидает появления элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    