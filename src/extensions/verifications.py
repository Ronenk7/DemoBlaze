from selenium.webdriver.support import expected_conditions as EC
from src.workflows.login_flow import LoginWorkFlows


class Verifications(LoginWorkFlows):
    """ This class contains generic methods that interact with the page UI. """

    def verify_inner_text_in_element_by_locator(self, expected: str, locator: tuple):
        self.wait.until(EC.visibility_of_element_located(locator))
        self.assertEqual(expected, self.driver.find_element(*locator).get_property("innerText").split(":")[1])

    def verify_inner_text_in_element(self, expected: str, elem):
        self.wait.until(EC.visibility_of(elem))
        self.assertEqual(expected, elem.get_property("innerText").split(":")[1])

    def verify_text_in_element_by_locator(self, expected: str, locator: tuple):
        self.wait.until(EC.visibility_of_element_located(locator))
        self.assertEqual(expected, self.driver.find_element(*locator).text)

    def verify_text_in_element(self, expected: str, elem):
        self.wait.until(EC.visibility_of(elem))
        self.assertEqual(expected, elem.text)

    def verify_text_in_element_text(self, expected: str, actual: str):
        self.assertEqual(expected, actual)

    def verify_is_display_by_locator(self, locator: tuple):
        self.wait.until(EC.visibility_of_element_located(locator))
        self.assertTrue(self.driver.find_element(*locator).is_displayed())

    def verify_is_display(self, elem):
        self.wait.until(EC.visibility_of(elem))
        self.assertTrue(elem.is_displayed())

    def verify_is_not_display(self, elem):
        self.wait.until(EC.invisibility_of_element(elem))
        self.assertFalse(elem.is_displayed())

    # def verify_inner_text_in_element_with_soft_assert(self, expected: str, locator: tuple):
    #     self.soft_assert(self.assertEqual, expected,
    #                      self.driver.find_element(*locator).get_property("innerText").split(":")[1])

    def verify_table_cells_text(self, search_column, search_text, return_columnText, expected_text):
        table_result_text = self.get_table_cells_text_by_xpath(search_column, search_text, return_columnText)
        self.assertTrue(table_result_text == expected_text)
