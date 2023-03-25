import pytest
import requests


@pytest.fixture(autouse=True)
def inform_method():
    print()
    print("\nMethod DELETE")


class TestDeleteMethod():

    @pytest.mark.delete
    @pytest.mark.delete_api
    @pytest.mark.parametrize('index, st_code', [("users/2", 204)])
    def test_delete_DELETE(self, index, st_code):
        response = requests.delete(f"https://reqres.in/api/{index}")
        assert response.status_code == st_code, "Неверный статус код"
        
        
        print("Status_code: ",response.status_code)
        print("URL: ", response.url)
        print() 
        print("Body: ")
        print(response.text)
    