import pytest
import requests

name = "morpheus"
job = "zion resident"
payload1 = {"name": "morpheus", "job": "zion resident"}

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod PUT")
    

class TestPUTMethod():
    
    @pytest.mark.put
    @pytest.mark.put_api
    @pytest.mark.parametrize("index, st_code", [("users/2", 200)])
    def test_put_UPDATE(self, index, st_code):
        response = requests.put(f"https://reqres.in/api/{index}", data = payload1)
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
    