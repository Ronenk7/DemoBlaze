from time import sleep
from allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.extensions.actions_element import ActionsElement


class ActionsBrowser(ActionsElement):
    """ This class contains generic methods that interact with the page UI. """

    @step("Switching Tabs")
    def switch_tab(self, tab_num: int) -> None:
        """
        Switches between the open tabs of the browser.
        Original tab == 0.
        New tabs number follows +1 logic.

        :param tab_num: number of the request tab
        """
        self.driver.switch_to.window(self.driver.window_handles[tab_num])

    @step("Refresh Page")
    def refresh_page(self) -> None:
        """Refreshes the page"""
        self.driver.get().refresh()

    @step("Takes screenshot")
    def take_screenshot(self, save_directory: str) -> None:
        """
        Takes a screenshot and saves it to a designated folder.

        param: save_directory: path to save the screenshot
        """
        sleep(1)
        self.driver.get().save_screenshot(f"{save_directory}.png")

    @step("Hide All Iframes")
    def hide_all_iframes(self):
        """ Locates all iframes in the webpage and changes their hidden property to "True". """

        all_iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        if len(all_iframes) > 0:
            print(f"{len(all_iframes)} Ad/s Found!\n")
            self.driver.execute_script(
                """
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                     {
                         elems[i].hidden=true;
                     }
                                  """
            )
        else:
            print("No frames found")

    @step("Accept Alert")
    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(0.5)

    @step("Get Text From Alert")
    def get_text_from_alert(self) -> str:
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        sleep(0.5)
        return alert_text

    @step("Close Alert")
    def close_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()
        sleep(0.5)
