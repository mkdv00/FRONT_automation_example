import pytest

from ..Pages.YandexPage import SearchHelper


class TestYandexSearchPage:
    
    @pytest.mark.smoke
    @pytest.mark.search
    def test_yandex_search(self, browser):
        yandex_page = SearchHelper(browser)
        yandex_page.go_to_site()
        yandex_page.enter_word("I love python")
        yandex_page.click_on_the_search_button()
        elements = yandex_page.check_navigation_bar()
        assert "Картинки\nВидео\nКарты\nТовары\nНовости\nПереводчик\nВсе" in elements

