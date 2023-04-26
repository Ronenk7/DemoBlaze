from src.extensions.verifications import Verifications
from src.pageObjects.login_page import LoginPage
from src.pageObjects.shared_pages.top_bar_page import TopBarPage


class LoginTests(Verifications):

    def setUp(self):
        super().setUp()
        """ Initializing the relevant page-objects for the "Login" tests """
        self.top_bar = TopBarPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.verify_text_in_element(self.config()["expected login"], self.top_bar.get_btn_login())

    def test_01_verify_properly_login(self):
        self.login_to_demo_blaze(self.config()["user_name"][0], self.config()["password"][0])
        self.verify_text_in_element(self.config()["expected_valid"], self.top_bar.get_txt_welcome())

    def test_02_verify_login_with_no_input(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][1], self.config()["password"][1])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    def test_03_verify_login_with_just_user_name(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][0], self.config()["password"][1])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    def test_04_verify_login_with_just_password(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][1], self.config()["password"][0])
        self.verify_text_in_element_text(self.config()["expected_invalid1"], alert_text)

    def test_05_verify_login_with_case_sensitive_user_name(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][2], self.config()["password"][0])
        self.verify_text_in_element_text(self.config()["expected_invalid2"], alert_text)

    def test_06_verify_login_with_case_sensitive_password(self):
        alert_text = self.login_to_demo_blaze_with_no_user_name_input(
            self.config()["user_name"][0], self.config()["password"][2])
        self.verify_text_in_element_text(self.config()["expected_invalid2"], alert_text)
