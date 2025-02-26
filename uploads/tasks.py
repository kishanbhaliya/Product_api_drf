import json
from celery import shared_task
from django.core.files.storage import default_storage
from categories.models import Category  # ✅ Correct import
from products.models import Product  # ✅ Correct import

@shared_task
def process_bulk_upload(file_path):
    """
    Celery task to process the uploaded JSON file and insert data into the database.
    """
    try:
        with default_storage.open(file_path, 'r') as file:
            data = json.load(file)

        categories = data.get("categories", [])
        products = data.get("products", [])

        category_mapping = {}  # Store created categories to avoid duplicate queries
        for cat in categories:
            category, created = Category.objects.get_or_create(
                id=cat["id"],
                defaults={
                    "name": cat["category_name"],
                    "description": cat.get("description", "")
                }
            )
            category_mapping[cat["id"]] = category

        for prod in products:
            category = category_mapping.get(prod.get("category_id"))
            if category:
                Product.objects.get_or_create(
                    id=prod["id"],
                    defaults={
                        "name": prod["product_name"],
                        "description": prod.get("product_description", ""),
                        "price": prod["product_price"],
                        "currency": prod["currency"],
                        "stock_quantity": prod["stock_quantity"],
                        "sku": prod["sku"],
                        "image_url": prod["image_url"],
                        "category": category
                    }
                )

        default_storage.delete(file_path)

        return {"status": "success", "message": "File processed successfully"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
