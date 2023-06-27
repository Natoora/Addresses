from django.conf import settings

from addresses.serializers import AddressSerializer, CountrySerializer, StateSerializer

settings = getattr(settings, 'ADDRESSES_SETTINGS', {})

AddressSerializer = settings.get("ADDRESS_SERIALIZER", AddressSerializer)
CountrySerializer = settings.get("COUNTRY_SERIALIZER", CountrySerializer)
StateSerializer = settings.get("STATE_SERIALIZER", StateSerializer)
