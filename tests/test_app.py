import pytest
from src.main import app
from bs4 import BeautifulSoup

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    
    soup = BeautifulSoup(response.data, 'html.parser')
    text = soup.find('p').get_text()
    assert text == 'Olá!'
    
if '__main__' == __name__:
    pytest.main()