from django.test import TestCase

from tests.factories import FactoryModelFactory, UserFactory
from trading.models import Factory


from django.test import TestCase
from core.models import User

class UserTestCase(TestCase):
    fixtures = ['core/fixtures/user_fixture.json']

    def test_user_loaded_from_fixture(self):
        # Ваш код для теста
        user_count = User.objects.count()
        self.assertNotEqual(user_count, 0)


class FactoryModelTestCase(TestCase):
    def setUp(self):
        # Создание фабрики с указанием пользователя
        self.factory = FactoryModelFactory()

    def test_factory_creation(self):
        """Тестирование создания фабрики."""
        self.assertEqual(self.factory.name, "Test Factory")
        self.assertEqual(self.factory.country, "Test Country")
