import allure
from tests.base_test import BaseTest


@allure.feature("Test main page")
class TestMainPage(BaseTest):

    def test_main_page_title(self):
        self.main_page.open()

        assert self.main_page.title == "ЕФРСБ", \
            f"Incorrect browser title:{self.main_page.title}"


@allure.feature("Test footer")
class TestFooter(BaseTest):

    def test_navigate_to_fedresurs(self):
        """ Navigate to Fedresurs """

        self.main_page.open()
        fedresurs_main_page = self.main_page.navigate_to_fedresurs()

        assert fedresurs_main_page.is_page_loaded(), \
            "Fedresurs project page not loaded"

    def test_navigate_to_bidding(self):
        """ Navigate to bidding """

        self.main_page.open()
        fedresurs_search_bidding_page = self.main_page.navigate_to_bidding()

        assert fedresurs_search_bidding_page.is_page_loaded(), \
            "Fedresurs search bidding page not loaded"

    def test_navigate_to_eaeu(self):
        """ Navigate to EAEU """

        self.main_page.open()
        eaeu_page = self.main_page.navigate_to_eaeu()

        assert eaeu_page.is_page_loaded(), \
            "Eaeu page not loaded"

    def test_navigate_to_monitoring(self):
        """ Navigate to Monitoring """

        self.main_page.open()
        fedresurs_monitoring_page = self.main_page.navigate_to_monitoring()

        assert fedresurs_monitoring_page.is_page_loaded(), \
            "Fedresurs monitoring page not loaded"

    def test_navigate_to_news(self):
        """ Navigate to News """

        self.main_page.open()
        fedresurs_news_page = self.main_page.navigate_to_news()

        assert fedresurs_news_page.is_page_loaded(), \
            "Fedresurs news page not loaded"

    def test_navigate_to_about_project(self):
        """ Navigate to About Project """

        self.main_page.open()
        fedresurs_about_project_page = \
            self.main_page.navigate_to_about_project()

        assert fedresurs_about_project_page.is_page_loaded(), \
            "Fedresurs about project page not loaded"

    def test_navigate_to_help(self):
        """ Navigate to Help """

        self.main_page.open()
        fedresurs_help_page = self.main_page.navigate_to_help()

        assert fedresurs_help_page.is_page_loaded(), \
            "Fedresurs help page not loaded"


    def test_support_email(self):
        """ Check support email """

        self.main_page.open()
        email = self.main_page.get_support_email()

        assert email == "help@fedresurs.ru"


    def test_support_phones(self):
        """ Check phones number """

        self.main_page.open()
        phones = self.main_page.get_support_phones()

        assert phones == "+7 (495) 989-73-68 +7 (800) 555-02-24"
