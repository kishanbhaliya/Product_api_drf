from rest_framework import serializers

class BulkUploadSerializer(serializers.Serializer):
    """Serializer for uploading JSON file"""
    file = serializers.FileField()
