from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import json
import time

URL = 'https://library.busan.go.kr/gsmbooks/member/login'

def main():
    try:
        driver = get_driver()
        driver.get(URL)

        config = get_config()
        print(config['userId'])
        print(config['userPw'])

        login_Lib_exe_script(driver, config['userId'], config['userPw'])

    except Exception as e:
        print(str(e))
    else:
        print('Main process is done.')
    finally:
        os.system('Pause')
        driver.quit()

def get_config():
    try:
        with open('config.json') as json_file:
            json_data = json.load(json_file)
    except Exception as e:
        print('Error in reading config file, {}'.format(e))
        return None
    else:
        return json_data

def login_Lib(driver, id, pw):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#id'))
    )
    print(type(id), id)
    element.send_keys(id)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#password'))
    )
    element.send_keys(pw)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input.btn_global'))
    )
    element.click()

    return False

def login_Lib_exe_script(driver, id, pw):
    script = " \
    (function execute(){
        document.querySelector('#id').value = '"+ id + "'; \
        document.querySelector('#password').value = '"+ pw + "'; \
    })();"
    driver.execute_script(script)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input.btn_global'))
    )
    element.click()
    return False

def get_driver():
    driver = webdriver.Chrome(r'C:\chromedriver.exe')
    driver.implicitly_wait(3)
    return driver

if __name__ == '__main__':
    main()
