class LoggedInHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logout_class = "user-signout"

    def click_login_avatar(self, email):
        self.driver.find_element_by_css_selector("[alt='" + email + "']").click()

    def click_logout(self):
        self.driver.find_element_by_class_name(self.logout_class).click()
