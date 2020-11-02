class Locators():
    #driver
    driver_path = "C:/Users/User/Desktop/Selenium/chromedriver.exe"

    #login page objects
    login_open_locators = "//a[@data-nav-ref = 'nav_ya_signin']"
    email_textbox_locators = "email"
    password_textbox_locators = "ap_password"
    login_password_button_locators = "signInSubmit"
    login_email_button_locators = "continue"

    #search page objects
    search_textbox_locators = "twotabsearchtextbox"
    search_button_locators = "//input[@value = 'Go']"
    search_secondpage_locators = "//li[@class = 'a-last']//a"
    secondpage_locators = "(//ul[@class = 'a-pagination']//li//a)[3]"
    product_locators = "((//div[@data-index = 2])[1]//a)[1]"

    #product page objects
    addToWishlist_button_locators = "add-to-wishlist-button-submit"
    go_to_deleteProductWishlistPage_locators = "(//span[@class = 'w-button-text'])[1]"
    delete_from_wishlist_locators = "(//a[contains(@class, 'a-link-normal a-declarative g-visible-js')])[1]"
    productText1 = "//li[@class = 'w-asin']//a"
    productText2 = "((//li[contains(@class, 'item-sortable')])[1]//a)[3]"
