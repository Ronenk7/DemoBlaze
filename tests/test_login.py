from src.extensions.verifications import Verifications
from src.pageObjects.login_page import LoginPage
from src.pageObjects.shared_pages.top_bar_page import TopBarPage
from allure_commons.types import Severity
from allure import title, severity, step


class LoginTests(Verifications):

    def setUp(self):
        super().setUp()
        """ Initializing the relevant page-objects for the "Login" tests """
        self.top_bar = TopBarPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.verify_text_in_element(self.config()["expected login"], self.top_bar.get_btn_login())

    @title("Test01 - Verify Properly Login")
    @severity(Severity.NORMAL)
    @step("This Test Verify a Properly Login")
    def test_01_verify_properly_login(self):
        self.login_to_demo_blaze(self.config()["user_name"][0], self.config()["password"][0])
        self.verify_text_in_element(self.config()["expected_valid"], self.top_bar.get_txt_welcome())

    @title("Test02 - Verify Properly Login")
    @severity(Severity.NORMAL)
    @step("This Test Verify a Properly Login")
    def test_02_verify_login_with_no_input(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][1], self.config()["password"][1])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    @title("Test03 -  Login With Just the Username")
    @severity(Severity.NORMAL)
    @step("This Test Login With Just the Username")
    def test_03_verify_login_with_just_username(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][0], self.config()["password"][1])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    @title("Test04 - Verify Login With Just Password")
    @severity(Severity.NORMAL)
    @step("This Test Verify Login With Just the Password")
    def test_04_verify_login_with_just_password(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][1], self.config()["password"][0])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    @title("Test05 - Verify Login With Case Sensitive Username")
    @severity(Severity.NORMAL)
    @step("This Test Verify Login With Case Sensitive Username")
    def test_05_verify_login_with_case_sensitive_username(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][2], self.config()["password"][0])
        self.verify_text_in_element_text(self.config()["expected_invalid2"], alert_text)

    @title("Test06 - Verify Login With Case Sensitive Password")
    @severity(Severity.NORMAL)
    @step("This Test Verify Login With Case Sensitive Password")
    def test_06_verify_login_with_case_sensitive_password(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][0], self.config()["password"][2])
        self.verify_text_in_element_text(self.config()["expected_invalid2"], alert_text)
