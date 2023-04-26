from selenium.webdriver.common.by import By


class LoginPage:
    # ======== Login Page Locators ======== #
    header = By.XPATH, "//h5[@id='logInModalLabel' and text()='Log in']"
    user_name_header = By.XPATH, "//label[@for='log-name']"
    user_name_input_field = By.ID, "loginusername"
    password_header = By.XPATH, "//label[@for='log-pass' and text()='Password:']"
    password_input_field = By.ID, "loginpassword"
    btn_x = By.XPATH, "//h5[@id='logInModalLabel']/ancestor::div[@class='modal-header']/button[@aria-label='Close']"
    btn_close = By.XPATH, "//button[text()='Log in']/ancestor::div[@class='modal-footer']/button[text()='Close']"
    btn_login = By.XPATH, "//button[@onclick='logIn()' and text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

        # ======== Login Page WebElements ======== #
        self.get_header = lambda: self.driver.find_element(*self.header)
        self.get_user_name_header = lambda: self.driver.find_element(*self.user_name_header)
        self.get_user_name_input_field = lambda: self.driver.find_element(*self.user_name_input_field)
        self.get_password_header = lambda: self.driver.find_element(*self.password_header)
        self.get_password_input_field = lambda: self.driver.find_element(*self.password_input_field)
        self.get_btn_x = lambda: self.driver.find_element(*self.btn_x)
        self.get_btn_close = lambda: self.driver.find_element(*self.btn_close)
        self.get_btn_login = lambda: self.driver.find_element(*self.btn_login)
