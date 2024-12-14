# test_app.py

import sys
import os
import pytest
# Add the path to your project's directory
project_root = "E:/TCE NLP intern/tool-final 4"
sys.path.append(project_root)

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

# def test_annotation_route(client):
#     # You can test your 'annotation' route here
#     # Replace the following example with your specific test case
#     response = client.post('/annotation', data={'user_input': 'நாடாளுமன்றமும் உண்டு.'})
#     assert response.status_code == 200
#     # Add more assertions based on your route's expected behavior

# def test_iaa_score_route(client):
#     # You can test your 'iaa_score' route here
#     # Replace the following example with your specific test case
#     response = client.post('/iaa_score', data={'user_input': 'Test Input', 'tokens[]': ['token1'], 'lemma[]': ['lemma1'], 'upos[]': ['upos1'], 'xpos[]': ['xpos1'], 'deprel[]': ['deprel1']})
#     assert response.status_code == 200
#     # Add more assertions based on your route's expected behavior
