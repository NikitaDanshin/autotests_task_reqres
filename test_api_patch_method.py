import pytest
import requests

@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod PATCH")
    
payload1 = {"name": "morpheus", "job": "zion resident"}

class TestPatchMethod():

    @pytest.mark.patch
    @pytest.mark.patch_api
    @pytest.mark.parametrize('index', ["users/2"])
    def test_patch_UPDATE(self, index):
        response = requests.patch(f"https://reqres.in/api/{index}", data = payload1)
        assert response.status_code == 200, "Неверный статус код"
        assert response.json().get('name') == 'morpheus', "Несоответствие имени"
        assert response.json().get('job') == 'zion resident', "Несоответствие работы"
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
    