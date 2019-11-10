class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_address_textbox_id = "user_email"
        self.email_me_xpath = "//input[@type='submit']"

    def enter_email_address(self, email_address):
        self.driver.find_element_by_id(self.email_address_textbox_id).send_keys(email_address)

    def click_email_me(self):
        self.driver.find_element_by_xpath(self.email_me_xpath).click()

