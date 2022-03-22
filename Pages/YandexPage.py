from .BasePage import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".navigation")


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = [i.text for i in all_list if len(i.text) > 0]
        return nav_bar_menu
