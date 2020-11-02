from selenium.webdriver.common.by import By
from pomTests.homework5.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_locators = Locators.email_textbox_locators
        self.password_textbox_locators = Locators.password_textbox_locators
        self.login_email_button_locators = Locators.login_email_button_locators
        self.login_password_button_locators = Locators.login_password_button_locators
        self.login_open_locators = Locators.login_open_locators

    def assertPage(self):
        assert self.driver.current_url == "https://www.amazon.com/", "There is seen a problem"

    def open_LoginPage(self):
        self.driver.find_element(By.XPATH, self.login_open_locators).click()

    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_textbox_locators).send_keys(email)

    def click_email_login(self):
        self.driver.find_element(By.ID, self.login_email_button_locators).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_locators).send_keys(password)

    def click_password_login(self):
        self.driver.find_element(By.ID, self.login_password_button_locators).click()