import requests
import pytest
import main


def test_status_code():
    response = requests.get('https://petstore.swagger.io/v2/pet/' + main.pet_id)
    assert response.status_code == 200


def test_string_exists():
    response = requests.get('https://petstore.swagger.io/v2/pet/' + main.pet_id)
    assert response.json()['name'] == 'LeBron'

