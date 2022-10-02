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
    abbreviation = FuzzyText(length=3)
    country = factory.SubFactory(CountryFactory, name="USA")


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    content_type = factory.Iterator(ContentType.objects.all())
    object_id = FuzzyInteger(low=1, high=500)
    line1 = factory.Faker("address")
    postcode = factory.Faker("postcode")
    country = factory.SubFactory(
        CountryFactory,
        name=FuzzyChoice(
            [
                "Greece",
                "Austria",
                "Vietnam",
                "USA",
                "UK",
                "Spain",
                "Netherlands",
                "Italy",
                "Israel",
                "France",
                "Belgium",
            ]
        ),
    )
    city = factory.Faker("city")
    county = FuzzyText(length=4)
    state = factory.SubFactory(
        StateFactory,
        name=FuzzyChoice(["Wyoming", "Virginia", "Utah", "Tennessee", "Pennsylvania"]),
    )
    notes = FuzzyText(length=20)
    delivery_address = factory.Faker("pybool")
    billing_address = factory.Faker("pybool")
    latitude = FuzzyFloat(low=1, high=20)
    longitude = FuzzyFloat(low=1, high=20)
