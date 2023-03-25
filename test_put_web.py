import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import time

payload1 = {"name": "morpheus", "job": "zion resident"}

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod PUT")

class TestWebPutMethod():

    @pytest.mark.put
    @pytest.mark.put_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users/2")])
    def test_put_UPDATE_Web(self, browser, url_page, index):
        
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="put"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.put(f"https://reqres.in/api/{index}", data = payload1)
            api_status_code = str(response.status_code)
            name_user = response.json().get('name')
            job_user = response.json().get('job')
            api_body = response.text
            
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert name_user in web_body, "Ошибка в теле ответа: не совпадает имя"
            assert job_user in web_body, "Ошибка в теле ответа: не совпадает работа"
            
    
            
            