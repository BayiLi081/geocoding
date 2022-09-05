import requests

'''
    Geocoding
    convert human-readable addresses to coordinates (latitude and longitude).
'''
def get_latlon_from_address(address):
    if isinstance(address, str):
        url = "https://nominatim.openstreetmap.org/search?q={}&format=json".format(address)
        response = requests.get(url)
        data = response.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
    else:
        print("Input should be a string of the address")
    return lat, lon
