from django.urls import include, re_path
from rest_framework import routers

from addresses import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"address", views.AddressViewSet, basename="address")
router.register(r"address-states", views.StateViewSet, basename="address-states")
router.register(
    r"address-countries", views.CountryViewSet, basename="address-countries"
)

urlpatterns = [
    re_path(r"", include(router.urls)),
]
