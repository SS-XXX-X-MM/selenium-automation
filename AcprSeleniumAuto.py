from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By

import os
import random
import time


driver = webdriver.Chrome("/usr/bin/chromedriver")


def login():
    url = "http://13.40.12.147/"
    driver.get(url)
    driver.maximize_window()

    email = 'shubhamsharma@gmail.com'
    password = 'password'

    email_field = driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
    email_field.send_keys(email)
    time.sleep(1)
    password_field = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
    password_field.send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="agreecheckbox"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()

    title = driver.title.casefold()
    try:
        assert title == 'home'
        print("login successful!")
        return True
    except AssertionError:
        print("login unsuccessful!")
        return False

def upload_file():
    upload_menu = driver.find_element(By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[2]/div/div/button')
    upload_menu.click()
    time.sleep(1)
    upload_btn = driver.find_element(By.XPATH, '//*[@id="customFile"]')
    upload_btn.send_keys(os.path.join(os.getcwd(), 'static_docs', 'Copy_of_Wedding_planning_contract.docx'))
    time.sleep(1)
    random_msg = f'This is a random message: {random.random()}'
    description = driver.find_element(By.XPATH, '//*[@id="uploadFileModal"]/div/div/div[2]/form/div[2]/textarea')
    description.send_keys(random_msg)
    time.sleep(1)
    submit = driver.find_element(By.XPATH, '//*[@id="waitDisBtn"]')
    submit.click()



login()
time.sleep(2)
upload_file()



