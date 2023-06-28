from importlib import import_module

from django.conf import settings

from addresses.serializers import AddressSerializer, CountrySerializer, StateSerializer


def import_callable_or_path(callable_or_path):
    if hasattr(callable_or_path, '__call__'):
        return callable_or_path
    else:
        assert isinstance(callable_or_path, str)
        package, attr = callable_or_path.rsplit('.', 1)
        return getattr(import_module(package), attr)


settings = getattr(settings, 'ADDRESSES_SETTINGS', {})

AddressSerializer = import_callable_or_path(settings.get("ADDRESS_SERIALIZER", AddressSerializer))
CountrySerializer = import_callable_or_path(settings.get("COUNTRY_SERIALIZER", CountrySerializer))
StateSerializer = import_callable_or_path(settings.get("STATE_SERIALIZER", StateSerializer))
