import requests

url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/location/search"

querystring = {"zip":"11203","radius":"100"}

headers = {
    "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
    "X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
