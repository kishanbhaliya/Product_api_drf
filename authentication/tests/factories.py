import factory
from django.contrib.auth import get_user_model
from categories.models import Category, Product

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('word')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Faker('word')
    price = factory.Faker('random_number', digits=3)
    stock = factory.Faker('random_number', digits=2)
    category = factory.SubFactory(CategoryFactory)
