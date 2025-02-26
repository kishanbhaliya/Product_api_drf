from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import json

class BulkUploadTests(APITestCase):
    def setUp(self):
        self.admin_user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.admin_user)

    def test_bulk_upload(self):
        json_data = json.dumps({
            "categories": [{"name": "Electronics"}, {"name": "Clothing"}],
            "products": [{"name": "Laptop", "price": 1000, "stock": 10}]
        })
        file = SimpleUploadedFile("data.json", json_data.encode('utf-8'), content_type="application/json")
        response = self.client.post("/upload/", {"file": file})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
