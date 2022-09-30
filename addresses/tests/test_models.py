import random
import string

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

from addresses.models import Address
from addresses.tests.factories import (
    StateFactory,
    AddressFactory,
    CountryFactory,
)
from common.test.base_test import NatooraTestCase


class CountryTestCase(NatooraTestCase):
    """Country Model Test Cases"""

    def setUp(self):
        self.country_UK = CountryFactory.create(name="United Kingdom")

    ######################################
    # Attributes from model
    ######################################
    # name
    def test_name(self):
        """Test that the name value matches the one assigned in the setUp"""
        self.assertEqual(self.country_UK.name, "United Kingdom")

    def test_name_max_length(self):
        """Test that assigning a name value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=61)
        )
        with self.assertRaises(ValidationError):
            self.country_UK.name = exceed_limits
            self.country_UK.full_clean()


class AddressTestCase(NatooraTestCase):
    """Address Model Test Cases"""

    def setUp(self):
        try:
            cust_model = ContentType.objects.get(
                model="customer", app_label="customers"
            )
        except ContentType.DoesNotExist:
            cust_model = ContentType.objects.create(
                model="customer", app_label="customers"
            )

        self.address_UK = AddressFactory.create(
            content_type=cust_model,
            object_id=1,
            line1="Natoora Ltd/Unit 8.",
            postcode="SE164RA",
            country=CountryFactory(name="United Kingdom"),
            city="London",
            county="Greater London",
            notes="Under the railway",
            delivery_address=True,
            billing_address=True,
            latitude=1.1,
            longitude=2.3,
        )

    ######################################
    # Attributes from model
    ######################################
    # object_id
    def test_object_id(self):
        """Test that the object_id value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.object_id, 1)

    # TODO: THIS IS NOT THROWING ANY ERROR
    # def test_object_id_positive(self):
    #    """ Test that the object_id can only be positive """
    #    with self.assertRaises(IntegrityError):
    #        self.address_UK.object_id = -1
    #        self.address_UK.full_clean()

    # line1
    def test_line1(self):
        """Test that the line1 value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.line1, "Natoora Ltd/Unit 8.")

    def test_line1_max_length(self):
        """Test that assigning a line1 value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=101)
        )
        with self.assertRaises(ValidationError):
            self.address_UK.line1 = exceed_limits
            self.address_UK.full_clean()

    # postcode
    def test_postcode(self):
        """Test that the postcode value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.postcode, "SE164RA")

    def test_postcode_max_length(self):
        """Test that assigning a postcode value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=11)
        )
        with self.assertRaises(ValidationError):
            self.address_UK.postcode = exceed_limits
            self.address_UK.full_clean()

    # city
    def test_city(self):
        """Test that the city value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.city, "London")

    def test_city_max_length(self):
        """Test that assigning a city value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=31)
        )
        with self.assertRaises(ValidationError):
            self.address_UK.city = exceed_limits
            self.address_UK.full_clean()

    # county
    def test_county(self):
        """Test that the county value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.county, "Greater London")

    def test_county_max_length(self):
        """Test that assigning a county value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=31)
        )
        with self.assertRaises(ValidationError):
            self.address_UK.county = exceed_limits
            self.address_UK.full_clean()

    def test_county_null(self):
        """Test that county can be saved as null"""
        try:
            self.address_UK.county = None
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_county_blank(self):
        """Test that county can be saved as blank"""
        try:
            self.address_UK.county = ""
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")

    # notes
    def test_notes(self):
        """Test that the notes value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.notes, "Under the railway")

    # TODO: MAX LENGTH IS NOT ENFORCED AT DB LEVEL FOR TEXT FIELDS
    # def test_notes_max_length(self):
    #    """ Test that assigning a notes value greater than max_length will throw a Validation Error """
    #    exceed_limits = "".join(
    #        random.choices(string.ascii_letters + string.digits, k=2001)
    #    )
    #    with self.assertRaises(ValidationError):
    #        self.address_UK.notes = exceed_limits
    #        self.address_UK.full_clean()

    def test_notes_null(self):
        """Test that notes can be saved as null"""
        try:
            self.address_UK.notes = None
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_notes_blank(self):
        """Test that notes can be saved as blank"""
        try:
            self.address_UK.notes = ""
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")

    # delivery_address
    def test_delivery_address(self):
        """Test that the delivery_address value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.delivery_address, True)

    def test_delivery_address_default(self):
        """Test that the default value for delivery_address is True"""
        default = Address.objects.create(
            content_type=ContentType.objects.create(
                model="customer2", app_label="customers"
            ),
            object_id=2,
            line1="Natoora Ltd/Unit 8.",
            postcode="SE164RA",
            city="London",
        )

        self.assertEqual(default.delivery_address, True)

    # billing_address
    def test_billing_address(self):
        """Test that the billing_address value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.billing_address, True)

    def test_billing_address_default(self):
        """Test that the billing_address value for delivery_address is True"""
        default = Address.objects.create(
            content_type=ContentType.objects.create(
                model="customer3", app_label="customers"
            ),
            object_id=3,
            line1="Natoora Ltd/Unit 8.",
            postcode="SE164RA",
            city="London",
        )
        self.assertEqual(default.billing_address, True)

    # latitude
    def test_latitude(self):
        """Test that the latitude value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.latitude, 1.1)

    def test_latitude_null(self):
        """Test that latitude can be saved as null"""
        try:
            self.address_UK.latitude = None
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_latitude_blank(self):
        """Test that latitude can be saved as blank"""
        try:
            self.address_UK.latitude = ""
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")

    # longitude
    def test_longitude(self):
        """Test that the longitude value matches the one assigned in the setUp"""
        self.assertEqual(self.address_UK.longitude, 2.3)

    def test_longitude_null(self):
        """Test that longitude can be saved as null"""
        try:
            self.address_UK.longitude = None
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_longitude_blank(self):
        """Test that longitude can be saved as blank"""
        try:
            self.address_UK.longitude = ""
            self.address_UK.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")


class StateTestCase(NatooraTestCase):
    """State Model Test Cases"""

    def setUp(self):
        self.state_US = StateFactory.create(
            name="Alabama",
            abbreviation="AL",
            country=CountryFactory(name="United States"),
        )

    ######################################
    # Attributes from model
    ######################################
    # name
    def test_name(self):
        """Test that the name value matches the one assigned in the setUp"""
        self.assertEqual(self.state_US.name, "Alabama")

    def test_name_max_length(self):
        """Test that assigning a name value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=51)
        )
        with self.assertRaises(ValidationError):
            self.state_US.name = exceed_limits
            self.state_US.full_clean()

    def test_name_null(self):
        """Test that name can be saved as null"""
        try:
            self.state_US.name = None
            self.state_US.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_name_blank(self):
        """Test that name can be saved as blank"""
        try:
            self.state_US.name = ""
            self.state_US.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")

    # abbreviation
    def test_abbreviation(self):
        """Test that the abbreviation value matches the one assigned in the setUp"""
        self.assertEqual(self.state_US.abbreviation, "AL")

    def test_abbreviation_max_length(self):
        """Test that assigning a abbreviation value greater than max_length will throw a Validation Error"""
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=11)
        )
        with self.assertRaises(ValidationError):
            self.state_US.abbreviation = exceed_limits
            self.state_US.full_clean()

    def test_abbreviation_null(self):
        """Test that abbreviation can be saved as null"""
        try:
            self.state_US.abbreviation = None
            self.state_US.full_clean()
        except ValidationError:
            self.fail("Assigning a null value throws unexpected ValidationError")

    def test_abbreviation_blank(self):
        """Test that abbreviation can be saved as blank"""
        try:
            self.state_US.abbreviation = ""
            self.state_US.full_clean()
        except ValidationError:
            self.fail("Assigning a blank value throws unexpected ValidationError")


"""
class AddressModelTest(NatooraTestCase):

    def setUp(self):
        AddressTestData.setup()
        self.addresses = Address.objects.all()
        self.natoora = self.addresses.get(object_id=1)

    def tearDown(self):
        pass

    def test_get_all_addresses(self):
        self.assertGreater(len(self.addresses), 1)

    def test_get_address_line1(self):
        self.assertEqual(self.natoora.line1, 'Natoora Ltd/Unit 8.')

    def test_get_address_postcode(self):
        self.assertEqual(self.natoora.postcode, 'SE164RA')

    def test_get_address_country(self):
        self.assertEqual(self.natoora.country, 'United Kingdom')

    def test_get_address_city(self):
        self.assertEqual(self.natoora.city, 'London')

    def test_get_address_county(self):
        self.assertEqual(self.natoora.county, 'Greater London')

    def test_get_address_notes(self):
        self.assertEqual(self.natoora.notes, 'Under the railway')


class StateModelTest(NatooraTestCase):

    def setUp(self):
        AddressTestData().setup_countries()
        AddressTestData().setup_states()
        self.states = State.objects.all()
        self.first_state = State.objects.first()

    def tearDown(self):
        pass

    def test_get_all_states(self):
        self.assertGreater(len(self.states), 1)

    def test_get_state_name(self):
        self.assertEqual(self.first_state.name, State.STATE_CHOICES[0][0])

    def test_get_state_abbreviation(self):
        self.assertEqual(self.first_state.abbreviation, State.SHORTHAND_CHOICES[0][1])
"""
