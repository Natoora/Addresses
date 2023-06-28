from importlib import import_module

from django.conf import settings

from addresses.serializers import AddressSerializer, CountrySerializer, StateSerializer


def import_from_path(path):
    package, attr = path.rsplit('.', 1)
    return getattr(import_module(package), attr)


settings = getattr(settings, 'ADDRESSES_SETTINGS', {})

AddressSerializer = import_from_path(settings.get("ADDRESS_SERIALIZER", AddressSerializer))
CountrySerializer = import_from_path(settings.get("COUNTRY_SERIALIZER", CountrySerializer))
StateSerializer = import_from_path(settings.get("STATE_SERIALIZER", StateSerializer))
