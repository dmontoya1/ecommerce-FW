import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("******************** Test001Login **********************")
        self.logger.info("******************** Verifying Home Page Title **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.driver.close()
            self.logger.info("********************  Home Page Title test is passed **********************")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_home_page_title.png")
            self.driver.close()
            self.logger.info("********************  Home Page Title test is Failed **********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************** Test001Login **********************")
        self.logger.info("******************** Testing Login **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("********************  Login test is passed **********************")
            assert True
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.driver.close()
            self.logger.info("********************  Login test is failed **********************")
            assert False
