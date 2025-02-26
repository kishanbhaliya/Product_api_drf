from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="password123")

    def test_register_user(self):
        data = {"email": "newuser@example.com", "password": "password123"}
        response = self.client.post("/auth/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        data = {"email": "testuser@example.com", "password": "password123"}
        response = self.client.post("/auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_logout_user(self):
        login_response = self.client.post("/auth/login/", {"email": "testuser@example.com", "password": "password123"})
        refresh_token = login_response.data["refresh"]
        response = self.client.post("/auth/logout/", {"refresh": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
