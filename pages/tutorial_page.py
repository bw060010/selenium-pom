# Import necessary libraries
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TutorialPage:
    """Define a class for the TutorialPage using the Page Object Model (POM) design pattern"""

    def __init__(self, driver, logger):
        """Constructor method for the class

        Args:
            driver (selenium.webdriver): The driver instance is passed to the class
            logger (logging): Error logging
        """

        self.driver = driver
        self.logger = logger

    def fill_name(self, name):
        """Method to fill the name field

        Args:
            name (str): the 'name' value
        """
        try:
            name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        name_field.send_keys(name)

    def fill_email(self, email):
        """Method to fill the email field

        Args:
            email (str): the 'email' value
        """

        try:
            email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        email_field.send_keys(email)

    def fill_phone(self, phone):
        """Method to fill the phone field

        Args:
            phone (str): the 'email' value
        """
        try:
            phone_field = self.driver.find_element(By.ID, "phone")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        phone_field.send_keys(phone)

    def click_dropdown(self, dropdown_xpath, option_text):
        """Method to click the dropdown

        Args:
            dropdown_xpath (str): the XPATH locator
            option_text (str): the option text
        """
        try:
            dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        dropdown.click()

        try:
            dropdown = self.driver.find_element(
                By.XPATH, f"//a[text()='{option_text}']"
            )
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        dropdown.click()

    def click_gender(self, gender):
        """Method to click the gender dropdown

        Args:
            gender (str): the 'gender' value
        """
        self.click_dropdown("//button[@data-toggle='dropdown']", gender)

    def set_checkbox(self):
        """Method to set the checkbox"""
        try:
            checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        checkbox.click()

    def click_button(self):
        """Method to click the button"""
        try:
            button = self.driver.find_element(By.XPATH, "//button[text()='Click me!']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        button.click()

    def validate_name_entered(self):
        """Method to check if the validation message shows"""
        self.click_button()

        # Pause the script to wait for validation messages to load
        time.sleep(2)

        try:
            self.driver.find_element(
                "xpath", "//label[text()='Please enter your name']"
            )
            result_flag = True
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            # This pattern of catching all exceptions is ok when you are starting out
            result_flag = False
            print("Validation message for name NOT present")

        if result_flag:
            print("Validation message for name present")
