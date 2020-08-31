import pytest
import requests
import Config


def test_irovanie():






    enough = requests.post(url=Config.dictu["second"], json=Config.body)




    print(enough)

    print(enough.json())

    # Press the green button in the gutter to run the script.

    assert enough.status_code == 200

    assert enough.json()["success"]==True

def test_Iryna2():

    response=requests.get(Config.dictu["first"])
    print(response)
    print(response.status_code)
    print(response.json())
    print(response.cookies)
    print(response.headers)

    assert response.status_code == 404
    assert response.json()["success"]==False