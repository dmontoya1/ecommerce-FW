import pytest
import time
import string
import random
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test003AddCustomer:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("**************** Test 003 Add Customer ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login Success **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_on_customers_menu()
        self.add_customer.click_on_customers_menu_item()

        self.add_customer.click_on_add_new()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("a12345678")
        self.add_customer.set_first_name("Juan")
        self.add_customer.set_last_name("Kumar")
        self.add_customer.set_gender("Male")
        self.add_customer.set_dob("01/22/1992")
        self.add_customer.set_company_name("ilanalab")
        self.add_customer.set_customer_roles("Guests")
        self.add_customer.set_manager_of_vendor("Vendor 2")
        self.add_customer.set_admin_content("This is for testing")
        self.add_customer.click_on_save()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
