import pytest
from app import app, add_numbers, subtract_numbers

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route returns correct response"""
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Welcome to Flask Jenkins CI/CD Pipeline!'
    assert json_data['status'] == 'success'

def test_health_route(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
    assert json_data['service'] == 'flask-app'

def test_greet_route(client):
    """Test the greet endpoint with a name parameter"""
    response = client.get('/api/greet/Jenkins')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Hello, Jenkins!'
    assert json_data['status'] == 'success'

def test_add_numbers():
    """Test the add_numbers function"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    """Test the subtract_numbers function"""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(1, 1) == 0
    assert subtract_numbers(0, 5) == -5
