import pytest
from flaskr import app

test_model = {
    'name': "Pavlik",
    'username': "superpavlik",
    'password': "qwerty16",
    'user_group_id': "2",
}

test_client_with_database = {
    'name': "Pavlik",
    'username': "superpavlik",
    'password': "qwerty16",
    'user_group_id': "2",
}


def test_home_page(test_client):
    response = test_client.post('/api/users/add', json=test_model)
    assert response.status_code == 200
