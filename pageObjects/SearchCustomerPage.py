class SearchCustomer:
    # Add customer Page
    txt_email_id = "SearchEmail"
    txt_first_name_id = "SearchFirstName"
    txt_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"
    tbl_search_results_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.txt_email_id).clear()
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.txt_first_name_id).clear()
        self.driver.find_element_by_id(self.txt_first_name_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.txt_last_name_id).clear()
        self.driver.find_element_by_id(self.txt_last_name_id).send_keys(last_name)

    def click_search(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def get_no_of_rows(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))

    def get_no_of_columns(self):
        return len(self.driver.find_elements_by_xpath(self.table_columns_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_no_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range(1, self.get_no_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == name:
                flag = True
                break
        return flag
