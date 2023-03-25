import pytest
import requests

name = "morpheus"
job = "leader"
error_password = "{\"error\":\"Missing password\"}"
payload1 = {"name": "morpheus", "job": "leader"}
payload2 = {"email": "eve.holt@reqres.in", "password": "pistol"}
payload3 = {"email": "sydney@fif"}

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod POST")
    
    
class TestPostMethod():

    @pytest.mark.post
    @pytest.mark.post_api
    @pytest.mark.parametrize("index,st_code", [("users", 201)])
    def test_posting_CREATE(self, index, st_code):
        response = requests.post(f"https://reqres.in/api/{index}", data = payload1)
        assert response.status_code == st_code, "Неверный статус код"
        name_user = response.json().get('name')
        job_user = response.json().get('job')
        assert name_user == name, "Несоответствие имени"
        assert job_user == job, "Несоответствие работы"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
        
    @pytest.mark.post
    @pytest.mark.post_api
    @pytest.mark.parametrize("index,st_code", [("register", 200)])
    def test_posting_REGISTER_SUCCESSFUL(self, index, st_code):
        response = requests.post(f"https://reqres.in/api/{index}", data = payload2)
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
      
    @pytest.mark.post
    @pytest.mark.post_api
    @pytest.mark.parametrize("index,st_code", [("register", 400)])
    def test_posting_REGISTER_UNSUCCESSFUL(self, index, st_code):
        response = requests.post(f"https://reqres.in/api/{index}", data = payload3)
        assert response.status_code == st_code, "Неверный статус код"
        assert response.text == error_password, "Отличается ошибка"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
     
    @pytest.mark.post
    @pytest.mark.post_api
    @pytest.mark.parametrize("index,st_code", [("login", 200)])
    def test_posting_login_SUCCESSFUL(self, index, st_code):
        response = requests.post(f"https://reqres.in/api/{index}", data = payload2)
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
    
    @pytest.mark.post
    @pytest.mark.post_api
    @pytest.mark.parametrize("index,st_code", [("login", 400)])
    def test_posting_LOGIN_UNSUCCESSFUL(self, index, st_code):
        response = requests.post(f"https://reqres.in/api/{index}", data = payload3)
        assert response.status_code == st_code, "Неверный статус код"
        assert response.text == error_password, "Отличается ошибка"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
    