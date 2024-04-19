# Had to install this with 'pip install uszipcode'
from uszipcode import SearchEngine

# Used to convert zipcode to a city
def ZipToCity(zip_code):
    search = SearchEngine()
    zipcode = search.by_zipcode(zip_code)
    
    if zipcode:
        city = zipcode.major_city
        latitude = zipcode.lat
        longitude = zipcode.lng
        return city, latitude, longitude
    else:
        return "No city is found.", latitude, longitude


# Testing with Fargo
zip = '58401'
city, lat, long  = ZipToCity(zip)

if lat and long:
    print(str(lat))
    print(str(long))
    print(str(city))
