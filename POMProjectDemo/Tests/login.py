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

    # test_01
    @classmethod
    def test_01_login_valid(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("Admin")
        time.sleep(1)
        login.set_password("admin123")
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1.png")
        login.click_login()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1_1.png")

        time.sleep(3)

        homepage = HomePage(driver)
        homepage.click_welcome()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1_3.png")
        time.sleep(1)
        homepage.click_logout()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1_4.png")

        time.sleep(3)

    # test_02 _invalid_username
    @classmethod
    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("Admin123")
        time.sleep(1)
        login.set_password("admin123")
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test2.png")
        login.click_login()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test2_1.png")

        time.sleep(3)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test2_2.png")
        message = driver.find_element_by_xpath(By.XPATH,"").text
        self.assertEqual(message, "Invalid credentials123")

        time.sleep(3)

    # test_03 invalid_password
    @classmethod 
    def test_03_login_invalid_password(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("Admin")
        time.sleep(1)
        login.set_password("admin123123")
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test3.png")
        login.click_login()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test3_1.png")

        time.sleep(3)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test3_2.png")
        message = driver.find_element_by_xpath(By.XPATH,"").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(3)

    # test_04 invalid_username_password
    @classmethod
    def test_04_login_invalid_username_password(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("Admin123")
        time.sleep(1)
        login.set_password("admin123123")
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4.png")
        login.click_login()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4_1.png")

        time.sleep(3)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4_2.png")
        message = driver.find_element_by_xpath(By.XPATH,"").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(3)

    # test_05 invalid_blankUsername_balnkPassword
    @classmethod
    def test_05_login_invalid_blankUsername_blankPassword(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("")
        time.sleep(1)
        login.set_password("")
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4.png")
        login.click_login()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4_1.png")

        time.sleep(3)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test4_2.png")
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













