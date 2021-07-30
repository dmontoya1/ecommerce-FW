import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    link_customers_menu_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]"
    link_customers_menu_item_xpath = \
        "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    btn_add_new_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_first_name_xpath = "//input[@id='FirstName']"
    txt_last_name_xpath = "//input[@id='LastName']"
    rb_male_gender_id = "Gender_Male"
    rb_female_gender_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    txt_customer_roles_xpath = \
        "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    list_item_administrators_xpath = "//li[contains(text(),'Administrators')]"
    list_item_forum_moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    list_item_registered_xpath = "//li[contains(text(),'Registered')]"
    list_item_guests_xpath = "//li[contains(text(),'Guests')]"
    list_item_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_mgr_of_vendor_xpath = "//select[@id='VendorId']"
    txt_admin_content_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_menu(self):
        self.driver.find_element_by_xpath(self.link_customers_menu_xpath).click()

    def click_on_customers_menu_item(self):
        self.driver.find_element_by_xpath(self.link_customers_menu_item_xpath).click()

    def click_on_add_new(self):
        self.driver.find_element_by_xpath(self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.txt_password_xpath).send_keys(password)

    def set_customer_roles(self, role):
        self.driver.find_element_by_xpath(self.txt_customer_roles_xpath).click()
        time.sleep(1)
        if role == 'Registered':
            self.list_item = self.driver.find_element_by_xpath(self.list_item_registered_xpath)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element_by_xpath(self.list_item_administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_element_by_xpath(self.list_item_guests_xpath)
        elif role == 'Registered':
            self.list_item = self.driver.find_element_by_xpath(self.list_item_registered_xpath)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element_by_xpath(self.list_item_vendors_xpath)
        else:
            self.list_item = self.driver.find_element_by_xpath(self.list_item_guests_xpath)
        time.sleep(1)
        # self.list_item.click()
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drp_mgr_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rb_male_gender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rb_female_gender_id).click()
        else:
            self.driver.find_element_by_id(self.rb_male_gender_id).click()

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.txt_first_name_xpath).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_xpath(self.txt_last_name_xpath).send_keys(last_name)

    def set_dob(self, dob):
        self.driver.find_element_by_xpath(self.txt_dob_xpath).send_keys(dob)

    def set_company_name(self, company_name):
        self.driver.find_element_by_xpath(self.txt_company_name_xpath).send_keys(company_name)

    def set_admin_content(self, content):
        self.driver.find_element_by_xpath(self.txt_admin_content_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()
