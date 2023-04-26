# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.events import EventFiringWebDriver
# from selenium.webdriver.support.events import AbstractEventListener
# from time import sleep
#
#
# class ScreenshotListener(AbstractEventListener):
#     def on_exception(self, exception, driver):
#         screenshot_name = "exception.png"
#         driver.get_screenshot_as_file(screenshot_name)
#         print("Screenshot saved as '%s'" % screenshot_name)
#
#
# class TestDemo(unittest.TestCase):
#     def test_demo(self):
#         pjsdriver = webdriver.Chrome()
#         pjsdriver.maximize_window()
#         sleep(2)
#         d = EventFiringWebDriver(pjsdriver, ScreenshotListener())
#         d.get("https://demoblaze.com/")
#         d.find_element(By.ID, "login2").click()
#         sleep(1)
#         d.find_element(By.ID, "loginusername").send_keys("Ronen")
#         d.find_element(By.ID, "loginpassword").send_keys("ronen123")
#         d.find_element(By.XPATH, "//button[@onclick='logIn()' and text()='Log in']").click()
#         sleep(3)
#         assert ("Welcome Ronen1" == d.find_element(By.ID, "nameofuser").text)
#         d.quit()
# if __name__ == '__main__':
#     unittest.main()
# def string_reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return string_reverse(string[1:]) + string[0]
#
#
# s = "reversal"
# reverse = string_reverse(s)
# print(reverse)




