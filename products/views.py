from rest_framework import generics, permissions
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class ProductDeleteView(APIView):
    """Soft delete a product"""

    def delete(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
            product.is_deleted = True  # ✅ Soft delete instead of permanent delete
            product.save()
            return Response({"message": "Product soft deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)