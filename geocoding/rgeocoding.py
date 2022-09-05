import requests

'''
    Reverse-Geocoding
    convert coordinates (latitude and longitude) to human-readable addresses.
'''

def get_address_from_latlon(input):
    if isinstance(input, list) & (len(input) == 2):
        lat = input[0]
        lon = input[1]
        url = "https://nominatim.openstreetmap.org/reverse?lat={}&lon={}&format=json".format(lat, lon)
        response = requests.get(url)
        data = response.json()
        address = data["display_name"]
    else:
        print("Input should be a list with format of [lat, lon]")
    return address
