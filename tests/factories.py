import factory
from core.models import User
from trading.models import Factory



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "testuser"
    password = "testpass"

class FactoryModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Factory

    name = "Test Factory"
    country = "Test Country"
    user = factory.SubFactory(UserFactory)
