from selenium import webdriver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append("C:/Users/LENOVO/Desktop/ProjectSeleniumPOM")
from selenium.webdriver.common.by import By
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.homePage import HomePage
import HtmlTestRunner

import warnings

warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\driver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def test_01_login_valid(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username("Admin")
        time.sleep(1)
        login.enter_password("admin123")
        time.sleep(1)
        login.click_login()

        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test01.png")

        time.sleep(3)

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(3)

    @classmethod
    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        time.sleep(1)
        login.enter_password("admin123")
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test2_1.png")

        login.click_login()


        time.sleep(3)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test2_2.png")
        time.sleep(3)
        message = driver.find_element_by_xpath(By.XPATH,"").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\report"))













