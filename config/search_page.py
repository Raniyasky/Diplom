from selenium.webdriver.common.by import By
from config.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    SEARCH_INPUT  = (By.NAME, "kp_query")
    FILM_RESULT  = (By.CSS_SELECTOR, 'p.name a.js-serp-metrika[data-type="film"]')
    PERSON_RESULT  = (By.CSS_SELECTOR, 'p.name a.js-serp-metrika[data-type="person"]')
    SERIES_RESULT  = (By.CSS_SELECTOR, 'p.name a.js-serp-metrika[data-type="series"]')
    INVALID_RESULT = (By.CSS_SELECTOR, ".search_results_topText")
    
    def search(self, query: str) -> None:
        """Выполняет поиск по фильму"""
        search_input = self.wait_for_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        search_input.submit()

    def get_first_film_text(self) -> str:
        """Возвращает название фильма первого в списке"""
        return self.wait_for_element(*self.FILM_RESULT).text
    
    def get_first_person_text(self) -> str:
        """Возвращает имя актера первого в списке"""
        return self.wait_for_element(*self.PERSON_RESULT).text
    
    def get_first_series_text(self) -> str:
        """Возвращает название сериала первого в списке"""
        return self.wait_for_element(*self.SERIES_RESULT).text
    
    def number_results_text(self) -> str:
        """Возвращает текст кол-ва результатов"""
        full_text = self.wait_for_element(*self.INVALID_RESULT).text
        return full_text.split("•")[-1].strip().lower()

    def click_first_result(self) -> None:
        """Кликает на первую карточку фильма в результатах"""
        self.wait_for_element(*self.FILM_RESULT).click()