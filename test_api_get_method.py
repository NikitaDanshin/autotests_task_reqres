import pytest
import requests

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod GET")
    

    
class TestGetMethod():
    
    @pytest.mark.get
    @pytest.mark.get_api
    @pytest.mark.parametrize("index, st_code", [("users?delay=3", 200)])
    def test_getting_DELAYED_RESPONSE(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
        
    @pytest.mark.get
    @pytest.mark.get_api
    @pytest.mark.parametrize("index, st_code", [("users?page=2", 200)])
    def test_getting_LIST_USERS(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
     
    @pytest.mark.get
    @pytest.mark.get_api
    @pytest.mark.parametrize("index, st_code", [("users/2", 200)])    
    def test_getting_SINGLE_USER(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
    
    @pytest.mark.get
    @pytest.mark.get_api  
    @pytest.mark.parametrize("index, st_code", [("users/23", 404)])    
    def test_getting__SINGLE_USER_NOT_FOUND(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text) 
     
    @pytest.mark.get
    @pytest.mark.get_api
    @pytest.mark.parametrize("index, st_code", [("unknown", 200)]) 
    def test_getting_LIST_RESOURCE(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text) 
        
    @pytest.mark.get
    @pytest.mark.get_api   
    @pytest.mark.parametrize("index, st_code", [("unknown/2", 200)]) 
    def test_getting_SINGLE_RESOURCE(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)  
    
    @pytest.mark.get
    @pytest.mark.get_api
    @pytest.mark.parametrize("index, st_code", [("unknown/23", 404)]) 
    def test_getting_SINGLE_RESOURCE_NOT_FOUND(self, index, st_code):
        response = requests.get(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)