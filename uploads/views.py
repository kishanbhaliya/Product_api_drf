import json
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from uploads.tasks import process_bulk_upload

class BulkUploadView(APIView):
    """
    API endpoint to upload a JSON file containing categories and products.
    The file is processed in the background using Celery.
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        """
        Handles the upload of the JSON file.
        The file is saved temporarily, and its path is passed to Celery for processing.
        """
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        file_path = f"uploads/{file.name}"
        default_storage.save(file_path, file)

        # Trigger Celery task
        process_bulk_upload.delay(file_path)

        return Response({'message': 'File uploaded successfully, processing in background'}, status=status.HTTP_202_ACCEPTED)
