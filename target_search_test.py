'''
Course: CST205-01_FA22
Title: Target Walmart Project
Abstract:
Authors: Christopher Raya, Kyle Dowling, Ricardo Perez JR
Date: 12/05/2022
'''

import requests

url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/product/search"

querystring = {"store_id":"3991","keyword":"lamp","offset":"0","limit":"24","sponsored":"1","rating":"0"}

headers = {
    "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
    "X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
