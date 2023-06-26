from django.conf import settings

settings = getattr(settings, 'ADDRESSES_SETTINGS', {})

Address = settings.get("ADDRESS_MODEL", "models.Address")
Country = settings.get("COUNTRY_MODEL", "models.Country")
State = settings.get("STATE_MODEL", "models.State")
