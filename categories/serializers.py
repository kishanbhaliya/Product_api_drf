from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category Model"""

    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent", "subcategories"]

    def get_subcategories(self, obj):
        """Fetch all subcategories for a given category"""
        subcategories = obj.subcategories.all()
        return CategorySerializer(subcategories, many=True).data
