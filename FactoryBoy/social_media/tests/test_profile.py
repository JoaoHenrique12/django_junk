from django.test import TestCase
from .fake_objects import ProfileFactory, UserFactory

# Create your tests here.

class SimpleFakerObjects(TestCase):
    def test_names_created(self):
        user1 = UserFactory(username="HellSank")
        user2 = UserFactory()

        self.assertNotEqual(user2.username, "HellSank")
        self.assertEqual(user1.username, "HellSank")

    def test_multiples_users(self):
        users = UserFactory.create_batch(3)
        self.assertEqual(len(users), 3)


class ProfileConnectProfile(TestCase):

    def get_abt(self):
        trudy = ProfileFactory(user=UserFactory(username="Trudy"))
        alice = ProfileFactory(user=UserFactory(username="Alice"))
        bob = ProfileFactory(user=UserFactory(username="Bob"))

        return alice, bob, trudy

    def test_visibility_profile(self):
        alice, bob, trudy = self.get_abt()

        alice.profile_type = '-'
        bob.profile_type = '-'

