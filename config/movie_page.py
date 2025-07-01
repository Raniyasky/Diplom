from selenium.webdriver.common.by import By
from config.base_page import BasePage

class MoviePage(BasePage):
    
    TITLE = (By.TAG_NAME, "h1")

    def get_title(self) -> str:
        """Получает название фильма"""
        return self.wait_for_element(*self.TITLE).text