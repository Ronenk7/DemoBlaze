from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from src.extensions.actions_browser import ActionsBrowser
from allure import step


class LoginWorkFlows(ActionsBrowser):

    @step("Business Flow: Enter Username")
    def enter_username(self, username: str):
        """ Entering the username.

        param: username: the username
        """
        self.send_keys_to_element(self.login_page.get_user_name_input_field(), username)

    @step("Business Flow: Enter Password")
    def enter_password(self, password: str):
        """ Entering the password.

        param: password: the password
        """
        self.send_keys_to_element(self.login_page.get_password_input_field(), password)

    @step("Business Flow: Click Login Button")
    def click_login_button(self):
        """ Clicking on the login button. """
        self.wait.until(EC.element_to_be_clickable(self.login_page.get_btn_login()))
        self.scrolls_element_to_top_and_click(self.login_page.get_btn_login())

    @step("Business Flow: Login")
    def login_to_website(self, username: str, password: str):
        """ Completing all the login steps.

        param: username: the username
        param: password: the password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        sleep(0.5)

    @step("Business Flow: Login to Demo Blaze Website")
    def login_to_demo_blaze(self, user_name: str, password: str) -> None:
        self.scrolls_element_to_top_and_click(self.top_bar.get_btn_login())
        self.login_to_website(user_name, password)

    @step("Business Flow: Login to Demo Blaze Website With No Username Input")
    def login_to_demo_blaze_with_no_user_name_input(self, user_name: str, password: str) -> str:
        self.scrolls_element_to_top_and_click(self.top_bar.get_btn_login())
        self.login_to_website(user_name, password)
        alert_text = self.get_text_from_alert()
        self.accept_alert()
        return alert_text
