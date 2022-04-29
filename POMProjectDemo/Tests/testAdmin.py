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
from POMProjectDemo.Pages.admin import admin
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
    def test_admin(self):
        driver = self.driver
        driver.get("http://opensource-demo.orangehrmlive.com/")
        username = 'AbayESS'

        login = LoginPage(driver)
        time.sleep(3)

        login.set_username("Admin")
        time.sleep(1)
        login.set_password("admin123")
        time.sleep(1)
        login.click_login()
        time.sleep(2)

        # admin
        login = admin(driver)
        login.click_admin()
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\admin\\clickAdmin.png")
        login.setUsername('Aaliyah.Haq')
        time.sleep(1)
        login.set_employee_name("Aaliyah Haq")
        time.sleep(2)
        login.click_btn()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\admin\\clickBTN.png")
        time.sleep(2)
        login.click_reset()
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\admin\\clickReset .png")
        login.click_add()

        time.sleep(2)
        login.click_admin()
        time.sleep(1)
        login.click_ohrmList()
        time.sleep(1)
        login.click_delete()
        time.sleep(1)
        login.click_confirmation()
        time.sleep(1)
    
        # logout
        homepage = HomePage(driver)
        homepage.click_welcome()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1_3.png")
        time.sleep(1)
        homepage.click_logout()
        driver.save_screenshot("C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\img\\test1_4.png")

        time.sleep(3)

    


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\LENOVO\\Desktop\\ProjectSeleniumPOM\\POMProjectDemo\\report\\admin"))













