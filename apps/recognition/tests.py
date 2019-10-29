from django.test import TestCase
from django.urls import reverse


def test_faces_view_post(admin_client):
    url = reverse('recognition:faces')
    response = admin_client.post(url)
    assert response

