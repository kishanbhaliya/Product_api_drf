from rest_framework.test import APITestCase
from rest_framework import status
from categories.models import Category
from tests.factories import UserFactory, CategoryFactory

class CategoryTests(APITestCase):
    def setUp(self):
        self.admin_user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.admin_user)
    
    def test_create_category(self):
        data = {"name": "Electronics"}
        response = self.client.post("/category/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_categories(self):
        CategoryFactory.create_batch(3)
        response = self.client.get("/category/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_soft_delete_category(self):
        category = CategoryFactory()
        response = self.client.delete(f"/category/{category.id}/")
        category.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(category.is_deleted)
