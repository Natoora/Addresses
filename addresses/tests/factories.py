import factory
from django.contrib.contenttypes.models import ContentType
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat, FuzzyChoice

from addresses.models import Country, State, Address
from customers.models import Customer
from customers.tests.factories.customer import CustomerTestData


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


# LEGACY
class AddressTestData:
    @staticmethod
    def setup():
        """
        Create an address for all customers in system.
        """
        CustomerTestData.setup()
        address_list = list()
        AddressTestData().setup_countries()
        AddressTestData().setup_states()

        try:
            cust_model = ContentType.objects.get(
                model="customer", app_label="customers"
            )
        except ContentType.DoesNotExist:
            cust_model = ContentType.objects.create(
                model="customer", app_label="customers"
            )

        for c in Customer.objects.all():
            try:
                a = Address.objects.get(content_type=cust_model, object_id=c.id)
            except Address.DoesNotExist:
                a = Address.objects.create(
                    content_type=cust_model,
                    object_id=c.id,
                    line1="Natoora Ltd/Unit 8.",
                    postcode="SE164RA",
                    country=Country.objects.get(name="UK"),
                    city="London",
                    county="Greater London",
                    notes="Under the railway",
                    billing_address=True,
                    delivery_address=True,
                )
            address_list.append(a)
        return address_list

    @staticmethod
    def setup_countries():
        """
        Create country instances
        """

        countries = [
            "Belgium",
            "France",
            "Israel",
            "Italy",
            "Netherlands",
            "Spain",
            "UK",
            "USA",
        ]

        for country in countries:
            try:
                c = Country.objects.get(name=country)
            except Country.DoesNotExist:
                c = Country()
                c.name = country
            c.save()
            print("Country created: ", c)

    @staticmethod
    def setup_states():
        """
        Create all 50 US States
        """
        united_states = [
            {"name": "Alabama", "short_name": "AL"},
            {"name": "Alaska", "short_name": "AK"},
            {"name": "Arizona", "short_name": "AZ"},
            {"name": "Arkansas", "short_name": "AR"},
            {"name": "California", "short_name": "CA"},
            {"name": "Colorado", "short_name": "CO"},
            {"name": "Connecticut", "short_name": "CT"},
            {"name": "Delaware", "short_name": "DE"},
            {"name": "District Of Columbia", "short_name": "DC"},
            {"name": "Florida", "short_name": "FL"},
            {"name": "Georgia", "short_name": "GA"},
            {"name": "Hawaii", "short_name": "HI"},
            {"name": "Idaho", "short_name": "ID"},
            {"name": "Illinois", "short_name": "IL"},
            {"name": "Indiana", "short_name": "IN"},
            {"name": "Iowa", "short_name": "IA"},
            {"name": "Kansas", "short_name": "KS"},
            {"name": "Kentucky", "short_name": "KY"},
            {"name": "Louisiana", "short_name": "LA"},
            {"name": "Maine", "short_name": "ME"},
            {"name": "Maryland", "short_name": "MD"},
            {"name": "Massachusetts", "short_name": "MA"},
            {"name": "Michigan", "short_name": "MI"},
            {"name": "Minnesota", "short_name": "MN"},
            {"name": "Mississippi", "short_name": "MS"},
            {"name": "Missouri", "short_name": "MO"},
            {"name": "Montana", "short_name": "MT"},
            {"name": "Nebraska", "short_name": "NE"},
            {"name": "Nevada", "short_name": "NV"},
            {"name": "New Hampshire", "short_name": "NH"},
            {"name": "New Jersey", "short_name": "NJ"},
            {"name": "New Mexico", "short_name": "NM"},
            {"name": "New York", "short_name": "NY"},
            {"name": "North Carolina", "short_name": "NC"},
            {"name": "North Dakota", "short_name": "ND"},
            {"name": "Ohio", "short_name": "OH"},
            {"name": "Oklahoma", "short_name": "OK"},
            {"name": "Oregon", "short_name": "OR"},
            {"name": "Pennsylvania", "short_name": "PA"},
            {"name": "Rhode Island", "short_name": "RI"},
            {"name": "South Carolina", "short_name": "SC"},
            {"name": "South Dakota", "short_name": "SD"},
            {"name": "Tennessee", "short_name": "TN"},
            {"name": "Texas", "short_name": "TX"},
            {"name": "Utah", "short_name": "UT"},
            {"name": "Vermont", "short_name": "VT"},
            {"name": "Virginia", "short_name": "VA"},
            {"name": "Washington", "short_name": "WA"},
            {"name": "West Virginia", "short_name": "WV"},
            {"name": "Wisconsin", "short_name": "WI"},
            {"name": "Wyoming", "short_name": "WY"},
        ]
        if State.objects.exists():
            # Don't repeat unnecessary work
            return
        for state in united_states:
            try:
                s = State.objects.get(name=state["name"])
            except State.DoesNotExist:
                s = State()
                s.name = state["name"]
            s.abbreviation = state["short_name"]
            s.country = Country.objects.get(name="USA")
            s.save()
            print("State created: ", s)

    @staticmethod
    def teardown():
        CustomerTestData.teardown()
        Address.objects.all().delete()
