from rest_framework.test import APITestCase
from rest_framework import status
from categories.models import Product
from tests.factories import UserFactory, ProductFactory

class ProductTests(APITestCase):
    def setUp(self):
        self.admin_user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.admin_user)

    def test_create_product(self):
        category = ProductFactory().category
        data = {
            "name": "Smartphone",
            "price": 699.99,
            "stock": 50,
            "category": category.id
        }
        response = self.client.post("/product/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        ProductFactory.create_batch(5)
        response = self.client.get("/product/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_soft_delete_product(self):
        product = ProductFactory()
        response = self.client.delete(f"/product/{product.id}/")
        product.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(product.is_deleted)
