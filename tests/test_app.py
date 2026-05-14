import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_cart_page():
    client = app.test_client()
    response = client.get("/cart")
    assert response.status_code == 200


def test_add_to_cart_redirect():
    client = app.test_client()
    response = client.get("/add/1")
    assert response.status_code == 302  # redirect after adding
