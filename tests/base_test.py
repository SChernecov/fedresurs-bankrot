import allure
import pytest
from pages.main_page import MainPage
from pages.eaeu_page import EaeuPage


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_ui(self, browser):
        self.browser = browser

    """ Fixture for screenshots and last url if tests failed """

    @pytest.fixture(autouse=True)
    def ui_report(self, request):
        yield
        if request.node.rep_call.failed:
            self.browser.set_page_load_timeout(1)
            if self.browser.session_id:
                allure.attach(self.browser.get_screenshot_as_png(),
                              "failure.png",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(self.browser.current_url, name="URL",
                              attachment_type=allure.attachment_type.URI_LIST)

    @property
    def main_page(self):
        return MainPage(self.browser)
