from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.name_textbox_id = "user_name"
        self.email_address_textbox_id = "user_email"
        self.password_textbox_id = "user_password"
        self.password_confirmation_textbox_id = "user_password_confirmation"
        self.agree_emails_checkbox_id = "user_unsubscribe_from_marketing_emails"
        self.agree_terms_checkbox_id = "user_agreed_to_terms"
        self.signup_button_xpath = "//input[@type='submit']"

    def enter_name(self, fullname):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.name_textbox_id))
        )
        element.send_keys(fullname)

    def enter_email_address(self, email_address):
        self.driver.find_element_by_id(self.email_address_textbox_id).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element_by_id(self.password_confirmation_textbox_id).send_keys(confirm_password)

    def agree_emails(self):
        self.driver.find_element_by_id(self.agree_emails_checkbox_id).click()

    def agree_terms(self):
        self.driver.find_element_by_id(self.agree_terms_checkbox_id).click()

    def click_signup(self):
        self.driver.find_element_by_xpath(self.signup_button_xpath).click()

