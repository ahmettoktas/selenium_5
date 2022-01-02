from selenium.webdriver.common.by import By


class parameters:
    driver_path = "chromedriver.exe"
    website_link = "https://www.amazon.com"
    email = "ahmettoktasdot@gmail.com"
    password = "159753"
    search_text = "samsung"


class login_page_locators:
    navigate_login_page = (By.CLASS_NAME, "nav-line-1-container")
    email = (By.NAME, "email")
    login_email = (By.ID, "continue")
    password = (By.ID, "ap_password")
    login = (By.ID, "signInSubmit")


class search_page_locators:
    search_textbox = (By.ID, "twotabsearchtextbox")
    search = (By.ID, "nav-search-submit-button")
    second_page = (By.CLASS_NAME, "a-last")
    product = (By.XPATH, "((//div[@data-index = 2])[1]//a)[1]")


class product_page_locators:
    add_to_wishlist = (By.ID, "add-to-wishlist-button-submit")
    product_text = (By.XPATH, "//ul[@class = 'w-product']//a")
    in_wishlist_product_text = (By.XPATH, "(//h3[@class = 'a-size-base']//a)[1]")
    wishlist = (By.CLASS_NAME, "w-button-inner")
    delete = (By.XPATH, "(//a[@class = 'a-link-normal a-declarative g-visible-js'])[1]")
