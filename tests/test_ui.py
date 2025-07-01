import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import BASE_URL
from config.search_page import SearchPage
from config.movie_page import MoviePage

# Тестовые данные
VALID_MOVIE = "Титаник"
INVALID_MOVIE = "asdasdasdfgh"
SERIES_NAME = "Игра в кальмара"
ACTOR_NAME = "Козловский"


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@allure.feature("UI Tests")
@allure.story("Поиск фильма по названию")
def test_search_movie(driver):
    with allure.step("Открыть главную страницу"):
        search_page = SearchPage(driver)
        search_page.open(BASE_URL)

    with allure.step(f"Искать фильм '{VALID_MOVIE}'"):
        search_page.search(VALID_MOVIE)

    with allure.step("Проверить, что первый результат содержит название"):
        first_result = search_page.get_first_film_text()
        assert VALID_MOVIE.lower() in first_result.lower()


@allure.feature("UI Tests")
@allure.story("Поиск сериала по названию")
def test_search_series(driver):
    with allure.step("Открыть главную страницу"):
        search_page = SearchPage(driver)
        search_page.open(BASE_URL)

    with allure.step(f"Искать фильм '{SERIES_NAME}'"):
        search_page.search(SERIES_NAME)

    with allure.step("Проверить, что первый результат содержит название"):
        first_result = search_page.get_first_series_text()
        assert SERIES_NAME.lower() in first_result.lower()


@allure.feature("UI Tests")
@allure.story("Поиск фильма с несуществующим названием")
def test_search_invalid_movie(driver):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Ввести несуществующее название"):
        search_page.search(INVALID_MOVIE)

    with allure.step("Проверить, что результатов нет"):
        invalid_result = search_page.number_results_text()
        assert "результаты: 0" in invalid_result.lower()


@allure.feature("UI Tests")
@allure.story("Открытие карточки фильма")
def test_open_movie_card(driver):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Искать фильм"):
        search_page.search(VALID_MOVIE)
        search_page.click_first_result()

    with allure.step("Проверить, что заголовок фильма отображается"):
        movie_page = MoviePage(driver)
        assert VALID_MOVIE.lower() in movie_page.get_title().lower()


@allure.feature("UI Tests")
@allure.story("Поиск актера через поиск")
def test_search_actor_first_result(driver):
    search_page = SearchPage(driver)
    search_page.open(BASE_URL)

    with allure.step("Ввести имя актера в строку поиска"):
        search_page.search(ACTOR_NAME)

    with allure.step("Убедиться, что первый результат — это Козловский"):
        first_result = search_page.get_first_person_text()
        assert ACTOR_NAME.lower() in first_result.lower()
