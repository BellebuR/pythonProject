import pytest
import requests
from Auto_test3 import get_random_cat_image_url

def test_get_random_cat_image_url_success(monkeypatch):
    class MockResponse:
        status_code = 200

        @staticmethod
        def json():
            return [{"url": "https://cdn2.thecatapi.com/images/123.jpg"}]

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    url = get_random_cat_image_url()
    assert url == "https://cdn2.thecatapi.com/images/123.jpg"

def test_get_random_cat_image_url_failure(monkeypatch):
    class MockResponse:
        status_code = 404

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    url = get_random_cat_image_url()
    assert url is None