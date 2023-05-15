import logging

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

logger = logging.getLogger(__name__)


class Country(models.Model):
    """
    Country model
    """

    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Address(models.Model):
    """
    Generic Address model
    """

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=36)
    content_object = GenericForeignKey("content_type", "object_id")
    line1 = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10, help_text="UK Postcode/US zip code")
    country = models.ForeignKey(
        "addresses.Country", on_delete=models.SET_NULL
    )
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30, null=True, blank=True)
    state = models.ForeignKey(
        "addresses.State", null=True, blank=True, on_delete=models.SET_NULL
    )
    notes = models.TextField(max_length=2000, null=True, blank=True)
    delivery_address = models.BooleanField(default=True)
    billing_address = models.BooleanField(default=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.line1

    def state_name(self):
        if self.state:
            return self.state.name
        return None

    def state_short_name(self):
        if self.state and self.state.abbreviation:
            return self.state.abbreviation
        return None

    def full_address(self):
        return "{} {} {}".format(self.line1, self.city, self.postcode)


class State(models.Model):
    """
    States model
    """

    name = models.CharField(max_length=40, null=True, blank=True)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    country = models.ForeignKey(
        "addresses.Country", null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = ("name", "country")

    def __str__(self):
        return self.name
