import json
import requests
import os



def test_create_user():  # Verify that allows creating a User

    url = "https://petstore.swagger.io/v2/user"
    payload = json.dumps({
        "id": 160911,
        "username": "test",
        "firstName": "test",
        "lastName": "test",
        "email": "test@mailinator.com",
        "password": "password",
        "phone": "777-77-77",
        "userStatus": 0
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.ok
    assert response.status_code == 200


# Verify that allows login as a User
def test_login():  # Verify that allows creating a User

    url = "https://petstore.swagger.io/v2/user/login?username=test&password=password"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    assert response.ok
    assert response.status_code == 200


def test_create_list_user():  # Verify that allows creating the list of Users
    url = "https://petstore.swagger.io/v2/user/createWithList"

    payload = json.dumps([
        {
            "id": 0,
            "username": "test1",
            "firstName": "test1",
            "lastName": "test1",
            "email": "test1",
            "password": "test1",
            "phone": "test1",
            "userStatus": 0
        },
        {
            "id": 2,
            "username": "test1",
            "firstName": "test1",
            "lastName": "test1",
            "email": "test1",
            "password": "test1",
            "phone": "test1",
            "userStatus": 0
        }
    ])
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    assert response.ok
    assert response.status_code == 200


def test_log_out():  # Verify that allows Log out User
    url = "https://petstore.swagger.io/v2/user/logout"

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    assert response.ok
    assert response.status_code == 200


def test_add_pet():  # Verify that allows adding a new Pet
    url = "https://petstore.swagger.io/v2/pet"

    payload = json.dumps({
        "id": 1232,
        "category": {
            "id": 1233,
            "name": "string"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.ok
    assert response.status_code == 200

def test_update_pet_image():  # Verify that allows updating Pet’s image
    url = "https://petstore.swagger.io/v2/pet/1232/uploadImage"
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'files_for_test', 'images', 'download.jfif')
    payload = {}
    files = [
        ('file', ('download.jfif', open(file_path, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'api_key': 'api_key'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    assert response.ok
    assert response.status_code == 200


# def test_update_data():# Verify that allows updating Pet’s name and status
    url = "https://petstore.swagger.io/v2/pet/1232"

    payload = {'name': ' totos',
               'status': ' busy'}
    files = [

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    assert response.ok
    assert response.status_code == 200

def test_delete_pet():  # Verify that allows deleting Pet
    url = "https://petstore.swagger.io/v2/pet/1232"

    payload = {}
    files = {}
    headers = {
        'api_key': 'api_key'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload, files=files)

    print(response.text)
    assert response.ok
    assert response.status_code == 200


