import factory

from faker import Faker
#from social_media.models import Profile #-> pylint didnt find with it.
from django.contrib.auth.models import User
from ..models import Profile, ProfileConnectProfile

fake = Faker()
Faker.seed(0)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.LazyAttribute(lambda obj: fake.user_name())
    email = factory.LazyAttribute(lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}@email.com")
    first_name = factory.LazyAttribute(lambda obj: fake.first_name())
    last_name = factory.LazyAttribute(lambda obj: fake.last_name())
