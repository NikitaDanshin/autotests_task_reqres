import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import time

payload1 = {"name": "morpheus", "job": "leader"}
payload2 = {"email": "eve.holt@reqres.in", "password": "pistol"}
payload3 = {"email": "sydney@fif"}

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod POST")

class TestWebPostMethod():

    @pytest.mark.post
    @pytest.mark.post_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users")])
    def test_posting_CREATE_Web(self, browser, url_page, index):
        
           
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="post"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.post(f"https://reqres.in/api/{index}", data = payload1)
            api_status_code = str(response.status_code)
            name_user = response.json().get('name')
            job_user = response.json().get('job')
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert name_user in web_body, "Ошибка в теле ответа: не совпадает имя"
            assert job_user in web_body, "Ошибка в теле ответа: не совпадает работа"
        
    @pytest.mark.post
    @pytest.mark.post_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "register")])
    def test_posting_REGISTER_SUCCESSFUL_Web(self, browser, url_page, index):
        
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="register-successful"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.post(f"https://reqres.in/api/{index}", data = payload2)
            api_status_code = str(response.status_code)
            
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Ошибка в теле ответа"
    
    @pytest.mark.post
    @pytest.mark.post_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "register")])
    def test_posting_REGISTER_UNSUCCESSFUL_Web(self, browser, url_page, index):
        
            
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="register-unsuccessful"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.post(f"https://reqres.in/api/{index}", data = payload3)
            api_status_code = str(response.status_code)
            
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Ошибка в теле ответа"
    
    @pytest.mark.post
    @pytest.mark.post_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "login")])
    def test_posting_login_SUCCESSFUL_Web(self, browser, url_page, index):
        
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="login-successful"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.post(f"https://reqres.in/api/{index}", data = payload2)
            api_status_code = str(response.status_code)
            
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Ошибка в теле ответа"
    
    @pytest.mark.post
    @pytest.mark.post_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "login")])
    def test_posting_login_UNSUCCESSFUL_Web(self, browser, url_page, index):
        
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="login-unsuccessful"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
            button1.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.post(f"https://reqres.in/api/{index}", data = payload3)
            api_status_code = str(response.status_code)
            
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Ошибка в теле ответа"
            
            