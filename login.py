from locators import login_page_locators
from locators import parameters
from base import BaseFunctions


class LoginFunctions(BaseFunctions):
    def assertPage(self):
        assert self.driver.current_url == parameters.website_link, "There is seen a problem"

    def navigate_to_login(self):
        self.click(login_page_locators.navigate_login_page)

    def login(self):
        self.input(login_page_locators.email, parameters.email)
        self.click(login_page_locators.login_email)
        self.input(login_page_locators.password, parameters.password)
        self.click(login_page_locators.login)
