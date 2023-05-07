from django.test import TestCase
from .fake_objects import UserFactory
from django.contrib.auth.models import User

# Create your tests here.

class SimpleFakerObjects(TestCase):
    def test_names_created(self):
        user1 = UserFactory(username="HellSank")
        user2 = UserFactory()
        print(user2.username)

        self.assertNotEqual(user2.username, "HellSank")
        self.assertEqual(user1.username, "HellSank")

    def test_multiples_users(self):
        users = UserFactory.create_batch(3)
        self.assertEqual(len(users), 3)
