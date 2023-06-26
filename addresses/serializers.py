from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from app_settings import Address, Country, State


class AddressesSerializer(serializers.ModelSerializer):
    """
    Address Serializer
    """

    content_type = serializers.CharField(write_only=True, required=True)
    app_label = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Address
        fields = (
            "id",
            "object_id",
            "line1",
            "delivery_address",
            "postcode",
            "country",
            "county",
            "state",
            "notes",
            "city",
            "billing_address",
            "app_label",
            "content_type",
            "state_name",
            "state_short_name",
            "latitude",
            "longitude",
        )

    def create(self, validated_data):
        model = validated_data.get("content_type", None)
        app_label = validated_data.get("app_label", None)
        a = Address()
        a.object_id = validated_data.get("object_id")
        a.content_type = ContentType.objects.get(model=model, app_label=app_label)
        a.billing_address = validated_data.get("billing_address", True)
        a.delivery_address = validated_data.get("delivery_address", True)
        a.line1 = validated_data.get("line1")
        a.postcode = validated_data.get("postcode")
        a.city = validated_data.get("city")
        a.county = validated_data.get("county")
        a.country = validated_data.get("country")
        a.state = validated_data.get("state")
        a.notes = validated_data.get("notes")
        a.latitude = validated_data.get("latitude")
        a.longitude = validated_data.get("longitude")
        a.save()

        return a

    def update(self, instance, validated_data):
        model = validated_data.get("content_type", None)
        app_label = validated_data.get("app_label", None)
        instance.object_id = validated_data.get("object_id", instance.object_id)
        instance.content_type = (
            ContentType.objects.get(model=model, app_label=app_label)
            if model and app_label
            else instance.content_type
        )
        instance.billing_address = validated_data.get(
            "billing_address", instance.billing_address
        )
        instance.delivery_address = validated_data.get(
            "delivery_address", instance.delivery_address
        )
        instance.line1 = validated_data.get("line1", instance.line1)
        instance.postcode = validated_data.get("postcode", instance.postcode)
        instance.city = validated_data.get("city", instance.city)
        instance.county = validated_data.get("county", instance.county)
        instance.country = validated_data.get("country", instance.country)
        instance.state = validated_data.get("state", instance.state)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.latitude = validated_data.get("latitude", instance.latitude)
        instance.longitude = validated_data.get("longitude", instance.longitude)
        instance.save()
        return instance


class StateSerializer(serializers.ModelSerializer):
    """
    State Serializer
    """

    class Meta:
        model = State
        fields = (
            "id",
            "name",
            "abbreviation",
            "country",
        )


class CountrySerializer(serializers.ModelSerializer):
    """
    Country Serializer
    """

    class Meta:
        model = Country
        fields = ("id", "name")
