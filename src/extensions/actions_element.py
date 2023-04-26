from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.webdriver_setup import WebDriverSetup


class ActionsElement(WebDriverSetup):
    """ This class contains generic methods that interact with the page UI. """

    def verify_visibility_of_elements(self, locators_list: list[tuple]) -> bool:
        """
        Clicks on an item that is located by a specified locator after verifying it is displayed.

        param: locators_list: a list of tuples. tuple, example: (By.ID, "Bob")
        """
        visible_elements = []
        for locator in locators_list:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if element:
                visible_elements.append("True")

        if len(visible_elements) != len(locators_list):
            return False
        return True

    def send_keys_to_visible_item(self, by_locator: tuple, value: str):
        """
        Sends keys to a field that is located by a specific locator after verifying
        it is displayed.

        param: by_locator: the web_element locator tuple, example: (By.ID, "Bob")
        param: value: the text to input in the field
        """
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def send_keys_to_element(self, by_element, value: str):
        """
        Sends keys to a field that is located by a specific element after verifying
        it is displayed.

        param: by_element: the web_element locator tuple, example: (By.ID, "Bob")
        param: value: the text to input in the field
        """
        self.wait.until(EC.visibility_of(by_element)).send_keys(value)

    def click_visible_item(self, by_locator: tuple) -> None:
        """
        Clicks on an item that is located by a specified locator after verifying it is displayed.

        param: by_locator: the web_element locator tuple, example: (By.ID, "Bob")
        """
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def scroll_and_hover_element(self, by_locator: tuple) -> None:
        """
        Scrolls the required element into view and mouse hover on it.

        param: by_locator: the web_element locator tuple, example: (By.ID, "Bob")
        """
        element = self.driver.find_element(*by_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_element_to_top(self, by_locator: tuple) -> WebElement:
        """
        Scrolls the element to the top of the page.

        param: by_locator: the web_element locator tuple, example: (By.ID, "Bob")
        """
        element = self.driver.find_element(*by_locator)
        element.location_once_scrolled_into_view
        return element

    def scrolls_element_to_top(self, elem) -> WebElement:
        """
        Scrolls the element to the top of the page.

        param: elem: the web_element locator tuple, example: (By.ID, "Bob")
        """
        elem.location_once_scrolled_into_view
        return elem

    def scroll_to_top_and_click(self, by_locator: tuple):
        """
        Scrolls element to top of the browser screen and clicks on it.

        param: by_locator: the web_element locator tuple, example: (By.ID, "Bob")
        """
        element = self.scroll_element_to_top(by_locator)
        element.click()
        sleep(0.5)

    def scrolls_element_to_top_and_click(self, elem):
        """
        Scrolls element to top of the browser screen and clicks on it.

        param: elem: the web_element
        """
        elem.location_once_scrolled_into_view
        self.wait.until(EC.visibility_of(elem))
        elem.click()
        sleep(0.5)

    def get_table_cell_text_by_xpath(self, table, search_column: int, search_text: str,
                                     return_column_text: int) -> str:
        table_xpath_by_id = f"//*[@id=\"{table.get_property('id')}\"]"
        # example: // *[ @ id = "tbodyid"] / tr / td[2][text() = 'Iphone 6 32gb'] / ancestor::tr / td[3]
        return_text_xpath = f"{table_xpath_by_id}/tr/td[{search_column}][text()='{search_text}']" \
                            f"/ancestor::tr/td[{return_column_text}]"

        return self.driver.find_element(By.XPATH, return_text_xpath).text

    def get_table_cells_text_by_xpath(self, table, search_column: int, return_column_text: int):
        table_xpath_by_id = f"//*[@id=\"{table.get_property('id')}\"]"
        # example: // *[ @ id = "tbodyid"] / tr / td[2] / ancestor::tr / td[3]
        return_text_xpath = f"{table_xpath_by_id}/tr/td[{search_column}]/ancestor::tr/td[{return_column_text}]"
        xpath = self.driver.find_elements(By.XPATH, return_text_xpath)
        return xpath
