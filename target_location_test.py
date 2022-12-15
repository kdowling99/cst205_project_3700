'''
Course: CST205-01_FA22
Title: Target Walmart Project
Abstract:
Authors: Christopher Raya, Kyle Dowling, Ricardo Perez JR
Date: 12/05/2022
'''

import requests
import json

url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/location/search"

querystring = {"zip":"93933","radius":"2"}

headers = {
    "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
    "X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

j = json.loads(response.text)
print(json.dumps(j, indent=4))

def json_print(response):
    j = json.loads(response.text)
    print(json.dumps(j,indent=2))
