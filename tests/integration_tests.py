from rest_framework.test import APITestCase
from rest_framework import status
from tests.factories import UserFactory, CategoryFactory, ProductFactory

class IntegrationTests(APITestCase):
    def setUp(self):
        self.admin_user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.admin_user)

    def test_full_category_product_flow(self):
        # Step 1: Create Category
        category_data = {"name": "Electronics"}
        category_response = self.client.post("/category/", category_data)
        self.assertEqual(category_response.status_code, status.HTTP_201_CREATED)
        category_id = category_response.data["id"]

        # Step 2: Create Product under Category
        product_data = {"name": "Smartphone", "price": 500, "stock": 20, "category": category_id}
        product_response = self.client.post("/product/", product_data)
        self.assertEqual(product_response.status_code, status.HTTP_201_CREATED)

        # Step 3: Retrieve Product
        product_id = product_response.data["id"]
        get_product_response = self.client.get(f"/product/{product_id}/")
        self.assertEqual(get_product_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_product_response.data["name"], "Smartphone")

        # Step 4: Soft Delete Product
        delete_response = self.client.delete(f"/product/{product_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
