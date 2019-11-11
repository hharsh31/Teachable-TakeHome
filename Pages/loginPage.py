from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "user_email"
        self.password_textbox_id = "user_password"
        self.login_button_xpath = "//input[@type='submit']"
        self.forgot_password_class = "link-below-button"
        self.create_account_xpath = "//a[contains(text(),'Create an Account')]"
        self.school_title_class = "school-title"

    def navigate_to_homepage(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.school_title_class))
        )
        element.click()

    def enter_username(self, *username):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.username_textbox_id))
        )
        element.send_keys(username)

    def enter_password(self, *password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def invalid_error_message_text(self):
        error = self.driver.find_element_by_class_name("alert").text
        return error

    def click_forgot_password(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.forgot_password_class))
        )
        element.click()

    def click_create_account(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.create_account_xpath))
        )
        element.click()

    def get_url(self):
        url = self. driver.current_url
        return url
