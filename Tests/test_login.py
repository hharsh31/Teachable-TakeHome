#!/usr/bin/env python3

import sys
import os
import pytest
from time import sleep

from faker import Faker
from selenium import webdriver
from Pages.loginPage import LoginPage
from Pages.createAccountPage import CreateAccountPage
from Pages.forgotPasswordPage import ForgotPasswordPage
from Pages.loggedOutHomePage import LoggedOutHomePage

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


class TestTeachableExam:

    faker = Faker()

    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome("/Users/hharsh/chromedriver")
        yield
        self.driver.close()

    def test_home_page_navigation(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        sleep(2)
        assert driver.title == "takehome"
        login.navigate_to_homepage()
        assert driver.title == "Homepage | takehome"

    def test_valid_login(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.enter_username("takehome@test.com")
        login.enter_password("Teachable")
        login.click_login()
        assert driver.page_source.__contains__("All Courses")
        assert driver.page_source.__contains__("My Courses")

    def test_invalid_email(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.enter_username("takehome@gmail.com")
        login.enter_password("Teachable")
        login.click_login()
        error = login.invalid_error_message_text()
        assert error == "Invalid email or password."

    def test_invalid_password(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.enter_username("takehome@test.com")
        login.enter_password("abc123")
        login.click_login()
        error = login.invalid_error_message_text()
        assert error == "Invalid email or password."

    def test_empty_email(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.enter_username()
        login.enter_password("Teachable")
        login.click_login()
        error = login.invalid_error_message_text()
        assert error == "Invalid email or password."

    def test_empty_password(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.enter_username("takehome@test.com")
        login.enter_password()
        login.click_login()
        error = login.invalid_error_message_text()
        assert error == "Invalid email or password."

    def test_forgot_password(self, test_setup):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.click_forgot_password()
        sleep(2)
        assert driver.page_source.__contains__("Reset Password")

        forgot_password = ForgotPasswordPage(driver)
        forgot_password.enter_email_address("takehome@test.com")
        forgot_password.click_email_me()
        assert driver.page_source.__contains__("You will receive an email with instructions on how to "
                                               "reset your password in a few minutes.")

    def test_create_account(self, test_setup, fullname=faker.name(), email_address=faker.email()):
        driver = self.driver

        driver.get("https://takehome.zeachable.com/")
        assert driver.title == "Homepage | takehome"

        loggedouthome = LoggedOutHomePage(driver)
        loggedouthome.click_login()

        login = LoginPage(driver)
        login.click_create_account()
        sleep(2)
        assert driver.page_source.__contains__("Sign Up to takehome")

        account = CreateAccountPage(driver)
        account.enter_name(fullname)
        account.enter_email_address(email_address)
        account.enter_password("Teachable")
        account.enter_confirm_password("Teachable")
        account.agree_emails()
        account.agree_terms()
        account.click_signup()
        assert driver.page_source.__contains__("All Courses")
        assert driver.page_source.__contains__("My Courses")

