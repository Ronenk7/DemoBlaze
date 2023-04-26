from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pageObjects.home_page import HomePage
from src.utilities.common_ops import CommonOps


class WebDriverSetup(CommonOps):

    def setUp(self) -> None:
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(float(self.config()["time_out"]))
            self.wait = WebDriverWait(self.driver, float(self.config()["time_out"]))
            self.driver.get("https://demoblaze.com/")
            self.assertEqual("STORE", self.driver.title)
            self.homepage = HomePage(self.driver)

            # Waiting for the last image of the cards to load
            self.wait.until(EC.visibility_of(self.homepage.get_cards_images()
                                             [(len(self.homepage.get_cards_images()) - 1)]))

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()
