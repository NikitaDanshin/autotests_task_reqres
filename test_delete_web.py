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
    print("\nMethod DELETE")

class TestWebDeleteMethod():

    @pytest.mark.delete
    @pytest.mark.delete_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users/2")])
    def test_delete_DELETE_Web(self, browser, url_page, index):
        
          
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="delete"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.delete(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Ошибка в теле ответа"
            
            
    
            
            