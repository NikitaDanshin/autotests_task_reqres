import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import time

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod GET")

class TestWebGetMethod():

    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users/2")])
    def test_getting_SINGLE_USER_Web(self, browser, url_page, index):
        
           
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button1 = browser.find_element(By.CSS_SELECTOR, '[data-id="users-single"]')
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
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"

           
        

    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users/23")])
    def test_getting_SINGLE_USER_NOT_FOUND_Web(self, browser, url_page, index):
           
            
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="users-single-not-found"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"
          
         
    @pytest.mark.get
    @pytest.mark.get_web       
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users?page=2")])
    def test_getting_LIST_USERS_Web(self, browser, url_page, index):
           
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="users"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"
    
    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "users?delay=3")])
    def test_getting_DELAYED_RESPONSE_Web(self, browser, url_page, index):
           

            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="delay"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            time.sleep(4)
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"
    
    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "unknown")])
    def test_getting_LIST_RESOURCE_Web(self, browser, url_page, index):
           

            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"
    
    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "unknown/2")])
    def test_getting_SINGLE_RESOURCE_Web(self, browser, url_page, index):
           

            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown-single"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            web_body = web_body.replace("\n","")
            web_body = web_body.replace(" ","")
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            api_body = api_body.replace(" ","")
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"

    @pytest.mark.get
    @pytest.mark.get_web
    @pytest.mark.parametrize("url_page, index", [("https://reqres.in/", "unknown/23")])
    def test_getting_SINGLE_RESOURCE_NOT_FOUND_Web(self, browser, url_page, index):
           
            browser.get(url_page)
            browser.implicitly_wait(5)
            
            button2 = browser.find_element(By.CSS_SELECTOR, '[data-id="unknown-single-not-found"]')
            browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
            button2.click()
            
            time.sleep(3)
            info_status_code = browser.find_element(By.CSS_SELECTOR, '[data-key="response-code"]')
            web_status_code = info_status_code.text
            info_body = browser.find_element(By.CSS_SELECTOR, '[data-key="output-response"]')
            web_body = info_body.text
            
            print("web status code: ", web_status_code)
            print("web body: ", web_body)
            
            response = requests.get(f"https://reqres.in/api/{index}")
            api_status_code = str(response.status_code)
            api_body = response.text
            
            print("api status code: ", api_status_code)
            print("api body: ", api_body)
            
            assert api_status_code == web_status_code, "Не совпадают статус коды"
            assert api_body == web_body, "Не совпадают тела запросов"