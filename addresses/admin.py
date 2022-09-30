from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from addresses.models import Country, State, Address


class AddressInLine(GenericStackedInline):
    """
    Address Inline.
    """

    model = Address
    fields = (
        "delivery_address",
        "billing_address",
        "line1",
        "postcode",
        "city",
        "country",
        "county",
        "state",
        "notes",
    )
    extra = 0


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Country Model Admin.
    """

    fields = ["name"]
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """
    State Model Admin.
    """

    fields = ["name", "abbreviation", "country"]
    list_display = ["name", "abbreviation", "country"]
    list_filter = ["country"]
    search_fields = ["name", "abbreviation", "country__name"]
