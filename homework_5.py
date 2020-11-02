from selenium import webdriver
from pomTests.homework5.locators import Locators
from pomTests.homework5.loginPage import LoginPage
from pomTests.homework5.searchPage import SearchPage
from pomTests.homework5.productPage import ProductPage
import time

driver_path = Locators.driver_path
driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get("https://www.amazon.com")

#login page
login = LoginPage(driver)
login.assertPage()
login.open_LoginPage()
login.enter_email("ahmettoktasdot@gmail.com")
login.click_email_login()
login.enter_password("159753")
login.click_password_login()

#search page
search = SearchPage(driver)
driver.implicitly_wait(1000)
search.enter_search_text("samsung")
driver.implicitly_wait(1000)
search.click_search_button()
search.click_second_page()
driver.implicitly_wait(1000)
search.click_product()

#product page
wishlist = ProductPage(driver)
wishlist.addToWishlist()
wishlist.goToDeletePage()
driver.implicitly_wait(2000)
wishlist.DeleteProduct()
time.sleep(3)
driver.quit()