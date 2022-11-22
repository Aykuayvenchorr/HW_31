from pytest_factoryboy import register

from .factories import CategoryFactory, UserFactory, AdFactory

pytest_plugins = "tests.fixtures"

register(CategoryFactory)
register(UserFactory)
register(AdFactory)