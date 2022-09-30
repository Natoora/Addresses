from rest_framework.test import APIClient

from addresses.tests.factories import AddressTestData
from common.test.authenticated_client import AuthenticatedClient
from common.test.base_test import NatooraTestCase


class AddressViewTests(NatooraTestCase):
    """Tests for the Address viewset"""

    def setUp(self):
        AddressTestData.setup()
        self.client = AuthenticatedClient().normal_client()
        self.uclient = APIClient()

    def test_auth(self):
        response = self.client.get("/api/address")
        self.assertEqual(response.status_code, 200)
        response = self.uclient.get("/api/address")
        self.assertEqual(response.status_code, 401)


class CountryViewTests(NatooraTestCase):
    """Tests for the Country view"""

    def setUp(self):
        AddressTestData.setup()
        self.client = AuthenticatedClient().normal_client()
        self.uclient = APIClient()

    def test_auth(self):
        response = self.client.get("/api/address-countries")
        self.assertEqual(response.status_code, 200)
        response = self.uclient.get("/api/address-countries")
        self.assertEqual(response.status_code, 401)
