from geocoding.geocoding import get_latlon_from_address
from geocoding.rgeocoding import get_address_from_latlon

lat, lon = get_latlon_from_address("Google Building 41, 1600 Amphitheatre Parkway, Mountain View, Santa Clara County, California, 94043, United States of America")

print(lat, lon)

print('----------------')

address = get_address_from_latlon([37.4224764, -122.0842499])

print(address)
