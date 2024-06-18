from home_page import SwagLabs
import pytest

url = "https://www.saucedemo.com/"
swaglabs_obj1 = SwagLabs(url)


# first test for checking correct title
def test_title():
    testing_data = "Swag Labs"
    assert swaglabs_obj1.fetch_title() == testing_data
    print("success : Test title pass")


# 2nd testcase for checking correct url
def test_url():
    testing_data = "https://www.saucedemo.com/inventory.html"
    assert swaglabs_obj1.fetch_url() == testing_data
    print("success : Test url pass")


# 3rd testcase for creating and writing in text file
def test_webpage_content():
    assert swaglabs_obj1.webpage_content() == True
    print("success : Test web_content pass")


# negative scenario for wrong username
def test_username():
    testing_username = "admin1"
    assert SwagLabs.username != testing_username
    print("failure :incorrect username")


# negative scenario for wrong password
def test_password():
    testing_username = "secret_sauce1"
    assert SwagLabs.password != testing_username
    print("success :incorrect password ")


# negative scenario to checl curret url with login url
def test_current_url():
    assert swaglabs_obj1.fetch_url() != url
    print("success : url not matching")


# Close the Python Selenium automation
def test_close():
    assert swaglabs_obj1.shutdown() is None
    print("SUCCESS : Python Selenium automation was success")
