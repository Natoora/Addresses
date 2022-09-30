from addresses.models import Address, Country
from addresses.tests.factories import AddressFactory
from common.test.authenticated_client import AuthenticatedClient
from common.test.base_test import NatooraTestCase


class TestAddressViewSet(NatooraTestCase):
    """
    Test Address.
    """

    def setUp(self):
        self.address = AddressFactory()
        self.client = AuthenticatedClient().normal_client()

    def test_get(self):
        response = self.client.get("/api/address")
        self.assertEqual(response.status_code, 200)
        number_of_addresses = Address.objects.count()
        self.assertEqual(len(response.data), number_of_addresses)

    def test_correct_post(self):
        response = self.client.post(
            "/api/address",
            {
                "object_id": 1,
                "line1": "piazzale Lotto 2, Milano",
                "delivery_address": True,
                "postcode": "20101",
                "country": 1,
                "county": None,
                "notes": None,
                "city": "Milano",
                "billing_address": True,
                "app_label": "suppliers",
                "content_type": "supplier",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_wrong_post(self):
        response = self.client.post("/api/address", {"line1": 1111111111112345678888})
        self.assertNotEqual(response.status_code, 200)

    def test_correct_put(self):
        response = self.client.put(
            "/api/address/{}".format(self.address.id),
            {
                "object_id": 1,
                "line1": "piazzale Lotto 2, Milano",
                "default": True,
                "postcode": "20101",
                "country": 1,
                "county": None,
                "notes": None,
                "city": "Milano",
                "billing_address": True,
                "app_label": "suppliers",
                "content_type": "supplier",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_wrong_put(self):
        response = self.client.put(
            "/api/address/{}".format(self.address.id),
            {
                "object_id": 1,
                # not sending line1 should break it
                # 'line1': 'piazzale Lotto 2, Milano',
                "default": True,
                "postcode": "20101",
                "country": "ITALY",
                "county": None,
                "notes": None,
                "city": "Milano",
                "billing_address": True,
                "app_label": "suppliers",
                "content_type": "supplier",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        before = Address.objects.count()
        self.client.delete("/api/address/{}".format(self.address.id))
        after = Address.objects.count()
        self.assertEqual(before, after + 1)


class TestAddressCountryView(NatooraTestCase):
    """
    Test AddressCountry.
    """

    def setUp(self):
        self.client = AuthenticatedClient().normal_client()

    def test_get(self):
        response = self.client.get("/api/address-countries")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Country.objects.count())
