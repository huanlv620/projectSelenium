from selenium.webdriver.common.by import By

class admin():

    def __init__(self, driver):
        self.driver = driver

        # user
        self.admin_link_id = "menu_admin_viewAdminModule"
        self.user_link_id = "searchSystemUser_userName"
        self.btn_link_id = "searchBtn"
        self.resetBtn_link_id = "resetBtn"
        self.employee_Name_link_id = "searchSystemUser_employeeName_empName"

        # add
        self.btnAdd_link_id = "btnAdd"
        
        #delete
        self.btnDelete_link_id = "btnDelete"
        self.ohrmList_link_id = "ohrmList_chkSelectRecord_10"
        self.confirmation_link_xpath = "/html/body/div[1]/div[3]/div[3]/div[3]/input[2]"


        
        
         
    def click_admin(self):
        self.driver.find_element_by_id(self.admin_link_id).click()

    def setUsername(self, username):
        self.driver.find_element_by_id(self.user_link_id).send_keys(username)

    def set_employee_name(self, employee):
        self.driver.find_element_by_id(self.employee_Name_link_id).send_keys(employee)
        
    def click_btn(self):
        self.driver.find_element_by_id(self.btn_link_id).click()

    def click_reset(self):
        self.driver.find_element_by_id(self.resetBtn_link_id).click()

    #add 
    def click_add(self):
        self.driver.find_element_by_id(self.btnAdd_link_id).click()

    #delete
    def click_delete(self):
        self.driver.find_element_by_id(self.btnDelete_link_id).click()

    def click_ohrmList(self):
        self.driver.find_element_by_id(self.ohrmList_link_id).click()

    def click_confirmation(self):
        self.driver.find_element_by_xpath(self.confirmation_link_xpath).click()