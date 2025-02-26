from django.urls import path
from uploads.views import BulkUploadView

urlpatterns = [
    path('bulk-upload/', BulkUploadView.as_view(), name='bulk-upload'),
]
