from addresses.tests.factories import CountryFactory, StateFactory


def populate():
    """Addresses create country entries"""
    CountryFactory.create(name="Greece")
    CountryFactory.create(name="Austria")
    CountryFactory.create(name="Vietnam")
    CountryFactory.create(name="USA")
    CountryFactory.create(name="UK")
    CountryFactory.create(name="Spain")
    CountryFactory.create(name="Netherlands")
    CountryFactory.create(name="Italy")
    CountryFactory.create(name="Israel")
    CountryFactory.create(name="Ireland")
    CountryFactory.create(name="France")
    CountryFactory.create(name="Belgium")

    """ Addresses create state entries """
    StateFactory.create(
        name="Wyoming", abbreviation="WY", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Wisconsin", abbreviation="WI", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="West_Virginia",
        abbreviation="WV",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Washington", abbreviation="WA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Virginia", abbreviation="VA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Vermont", abbreviation="VT", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Utah", abbreviation="UT", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Texas", abbreviation="TX", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Tennessee", abbreviation="TN", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="South_Dakota",
        abbreviation="SD",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="South_Carolina",
        abbreviation="SC",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Rhode_Island",
        abbreviation="RI",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Pennsylvania",
        abbreviation="PA",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Oregon", abbreviation="OR", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Oklahoma", abbreviation="OK", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Ohio", abbreviation="OH", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="North_Dakota",
        abbreviation="ND",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="North_Carolina",
        abbreviation="NC",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="New_York", abbreviation="NY", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="New_Mexico", abbreviation="NM", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="New_Jersey", abbreviation="NJ", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="New_Hampshire",
        abbreviation="NH",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Nevada", abbreviation="NV", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Nebraska", abbreviation="NE", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Montana", abbreviation="MT", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Missouri", abbreviation="MO", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Mississippi", abbreviation="MS", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Minnesota", abbreviation="MN", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Michigan", abbreviation="MI", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Massachusetts",
        abbreviation="MA",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Maryland", abbreviation="MD", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Maine", abbreviation="ME", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Louisiana", abbreviation="LA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Kentucky", abbreviation="KY", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Kansas", abbreviation="KS", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Iowa", abbreviation="IA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Indiana", abbreviation="IN", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Illinois", abbreviation="IL", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Idaho", abbreviation="ID", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Hawaii", abbreviation="HI", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Georgia", abbreviation="GA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Florida", abbreviation="FL", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="District_of_Columbia",
        abbreviation="DC",
        country=CountryFactory.create(name="USA"),
    )
    StateFactory.create(
        name="Delaware", abbreviation="DE", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Connecticut", abbreviation="CT", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Colorado", abbreviation="CO", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="California", abbreviation="CA", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Arkansas", abbreviation="AR", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Arizona", abbreviation="AZ", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Alaska", abbreviation="AK", country=CountryFactory.create(name="USA")
    )
    StateFactory.create(
        name="Alabama", abbreviation="AL", country=CountryFactory.create(name="USA")
    )
