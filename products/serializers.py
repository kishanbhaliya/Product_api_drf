from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product Model"""

    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "currency",
            "stock_quantity",
            "sku",
            "image_url",
            "created_at",
            "updated_at"
        ]
