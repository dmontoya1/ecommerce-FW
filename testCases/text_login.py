from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test001Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots/test_home_page_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("Screenshots/test_login.png")
            self.driver.close()
            assert False
