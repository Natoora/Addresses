import factory
from django.contrib.contenttypes.models import ContentType
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat, FuzzyChoice

from addresses.models import Country, State, Address


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country
        django_get_or_create = ("name",)

    name = factory.Faker("name")


class StateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = State
        django_get_or_create = ("name",)

    name = factory.Faker("name")


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        exclude = ["content_object"]
        abstract = True

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )
    object_id = factory.SelfAttribute("content_object.id")
    line1 = factory.Faker("address")
    postcode = factory.Faker("postcode")
    city = factory.Faker("city")
