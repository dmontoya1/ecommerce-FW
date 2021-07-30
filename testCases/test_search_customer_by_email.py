import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test004SearchCustomerByEmail:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("*********** Search Customer by Email 004 **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************ Login Success ***************")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_on_customers_menu()
        self.add_customer.click_on_customers_menu_item()

        self.logger.info("************ Search Customer by Email")
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.set_email("victoria_victoria@nopCommerce.com")
        self.search_customer.click_search()
        time.sleep(2)

        status = self.search_customer.search_customer_by_email("victoria_victoria@nopCommerce.com")
        self.driver.close()

        assert status

        self.logger.info("************ Test004SearchCustomerByEmail Finished ***********")
