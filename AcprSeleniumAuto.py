from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By



def get_driver():
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    return driver

def login(driver):
    url = "http://13.40.12.147/"
    driver.get(url)

    email = 'shubhamsharma@gmail.com'
    password = 'password'

    email_field = driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
    password_field.send_keys(password)

    driver.find_element(By.XPATH,'//*[@id="agreecheckbox"]').click()
    driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()

    title = driver.title.casefold()
    try:
        assert title == 'home'
        print("login successful!")
        return True
    except AssertionError:
        print("login unsuccessful!")
        return False



driver = get_driver()
login(driver)




