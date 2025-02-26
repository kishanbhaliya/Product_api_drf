from django.urls import path
from .views import RegisterView, LoginView, LogoutView, PasswordResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', PasswordResetView.as_view(), name='forgot-password'),
]
