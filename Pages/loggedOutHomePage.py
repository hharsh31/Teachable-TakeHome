class LoggedOutHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button_xpath = "//a[contains(text(),'Login')]"

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
