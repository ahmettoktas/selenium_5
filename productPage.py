from selenium.webdriver.common.by import By
from pomTests.homework5.locators import Locators
import time

class ProductPage():
    def __init__(self, driver):
        self.driver = driver

        self.addToWishlist_button_locators = Locators.addToWishlist_button_locators
        self.go_to_deleteProductWishlistPage_locators = Locators.go_to_deleteProductWishlistPage_locators
        self.delete_from_wishlist_locators = Locators.delete_from_wishlist_locators
        self.productText1 = Locators.productText1
        self.productText2 = Locators.productText2

    def addToWishlist(self):
        self.driver.find_element(By.ID, self.addToWishlist_button_locators).click()

    def goToDeletePage(self):
        textProduct1_1 = (self.driver.find_element(By.XPATH, self.productText1)).get_attribute("innerHTML")
        self.driver.find_element(By.XPATH, self.go_to_deleteProductWishlistPage_locators).click()
        time.sleep(1)
        textProduct2_1 = (self.driver.find_element(By.XPATH, self.productText2)).get_attribute("innerHTML")
        assert textProduct1_1[:20] == textProduct2_1[:20], "Bu iki ürün aynı değil."

    def DeleteProduct(self):
        textProduct2_1 = (self.driver.find_element(By.XPATH, self.productText2)).get_attribute("innerHTML")
        self.driver.find_element(By.XPATH, self.delete_from_wishlist_locators).click()
        print(self.driver.find_element(By.XPATH, self.productText2)).get_attribute("innerHTML")
        assert self.driver.find_element(By.XPATH, self.productText2) == textProduct2_1 , "There is a problem"

