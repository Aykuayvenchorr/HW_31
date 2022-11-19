import datetime

import factory

from ads.models import Category, Ad
from user.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    birth_date = datetime.date.today() - datetime.timedelta(days=5000)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = factory.Faker('name')
    category = factory.SubFaker(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 6666
