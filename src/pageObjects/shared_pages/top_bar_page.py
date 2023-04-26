from selenium.webdriver.common.by import By


class TopBarPage:
    # ======== Top Bar Page Locators ========#
    txt_header = By.XPATH, "//a[normalize-space()='PRODUCT STORE']"
    btn_home = By.XPATH, "//a[text()='Home ']"
    btn_contact = By.XPATH, "//a[text()='Contact']"
    btn_about_us = By.XPATH, "//a[text()='About us']"
    btn_cart = By.XPATH, " //a[text()='Cart']"
    btn_login = By.ID, "login2"
    btn_signup = By.ID, "signin2"
    txt_welcome = By.ID, "nameofuser"

    def __init__(self, driver):
        self.driver = driver

        # ======== Top Bar Page Elements ========#
        self.get_txt_header = lambda: self.driver.find_element(*self.txt_header)
        self.get_btn_home = lambda: self.driver.find_element(*self.btn_home)
        self.get_btn_contact = lambda: self.driver.find_element(*self.btn_contact)
        self.get_btn_about_us = lambda: self.driver.find_element(*self.btn_about_us)
        self.get_btn_cart = lambda: self.driver.find_element(*self.btn_cart)
        self.get_btn_login = lambda: self.driver.find_element(*self.btn_login)
        self.get_btn_signup = lambda: self.driver.find_element(*self.btn_signup)
        self.get_txt_welcome = lambda: self.driver.find_element(*self.txt_welcome)
