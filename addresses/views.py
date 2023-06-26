from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from addresses.serializers import (
    AddressesSerializer,
    CountrySerializer,
    StateSerializer,
)
from app_settings import Address, Country, State


class AddressViewSet(viewsets.ModelViewSet):
    """
    Customer view set
    """

    serializer_class = AddressesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Address.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    """
    Country view set
    """

    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Country.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    """
    State view set
    """

    serializer_class = StateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return State.objects.all()


def get_district_from_postcode(postcode):
    """
    function to get the district from a postcode
    """
    if settings.APP_LOCATION == "LONDON":
        try:
            stripped_postcode = postcode.replace(" ", "").upper()
            district = stripped_postcode[:-3]
        except Exception as e:
            return Response(
                {"message": f"Error with post code {postcode}: {e}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        try:
            stripped_zip_code = postcode.replace(" ", "")
            int(stripped_zip_code[0])
            district = stripped_zip_code[:5]
        except ValueError:
            return Response(
                {"message": "Invalid zipcode"}, status=status.HTTP_400_BAD_REQUEST
            )
        except IndexError:
            return Response(
                {"message": "Invalid zipcode"}, status=status.HTTP_400_BAD_REQUEST
            )
    return district
