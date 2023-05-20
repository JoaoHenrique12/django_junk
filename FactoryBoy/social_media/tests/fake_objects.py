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

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    profile_type = '+'
    like_read = False
    birth = fake.date_of_birth()

class ProfileConnectProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProfileConnectProfile
        django_get_or_create = ('sender_id','receiver_id',)

    sender_id = factory.SubFactory(ProfileFactory)
    receiver_id = factory.SubFactory(ProfileFactory)
    sender_status = 'U'
    receiver_status = 'U'
