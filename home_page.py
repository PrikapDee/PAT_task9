from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pathlib import Path


class SwagLabs:
    # username and password data

    username = "standard_user"
    password = "secret_sauce"
    # file path to create file
    filepath = Path("E:\Priyanka\workspace\selenium\webpage_task_11.txt")

    # locators
    username_locator = "user-name"
    password_locator = "password"
    xpath_login = "/html/body/div/div/div[2]/div[1]/div/di""v/form/input"
    xpath_content = "/html/body"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to fetch ur of webpage
    def fetch_url(self):
        if self.login_labs():
            sleep(5)
            return self.driver.current_url
        else:
            print("error in fetching the url")
            return False

    # login method to log in to application
    def login_labs(self):

        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.username)
        self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.xpath_login).click()
        sleep(3)
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("successful login")
            return True
        else:
            print("issue in login")
            return False

    #  method to create a text file and write data in file
    def webpage_content(self):
        if self.login_labs():
            page_content = self.driver.find_element(by=By.XPATH, value=self.xpath_content).text
            with open(self.filepath, "w") as file:
                file.write(page_content)
                print("file created")
                return True
        else:
            print("issue in file creation")
            return False

    # method to shut down browser
    def shutdown(self):
        self.driver.close()

    # method to fetch title of page
    def fetch_title(self):
        if self.login_labs():
            web_title = self.driver.title
            print("title captured")
            return web_title
        else:
            return "error in fetching title"
