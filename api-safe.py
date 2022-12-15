'''
Course: CST205-01_FA22
Title: Target Walmart Project
Abstract:
Authors: Christopher Raya, Kyle Dowling, Ricardo Perez JR
Date: 12/05/2022
'''

import requests
import json

class Product:
    ''' a class to model a product '''
    def __init__(self, name, store, purchase_url, image_url, price):
        self.name = name
        self.store = store
        self.purchase_url = purchase_url
        self.image_url = image_url
        self.price = price
    def __str__(self):
        #return f'{self.name} from {self.store}'
        return f'Name: {self.name}\nStore: {self.store}\nPrice: {self.price}'
    def __eq__(self, other):
        return self.purchase_url == other.purchase_url


productList = []

j = json.loads(input())
print(type(j))
# print(json.dumps(j["products"]))
for x in range(0,5):
    try:
        p = j["products"][x]
        name = p["item"]["product_description"]["title"]
        store = "Target"
        purchase_url = p["item"]["enrichment"]["buy_url"]
        image_url = p["item"]["enrichment"]["images"]["primary_image_url"]
        price = p["price"]["formatted_current_price"]
        productList.append(Product(name, store, purchase_url, image_url, price))
    except:
        print("error: failed to load product")

j = json.loads(input())
# print(json.dumps(j["data"]["search"]["searchResult"]["itemStacks"][0]["items"]))
for x in range(0,5):
    try:
        p = j["data"]["search"]["searchResult"]["itemStacks"][0]["items"][x]
        name = p["name"]
        store = "Walmart"
        purchase_url = "www.walmart.com" + p["canonicalUrl"]
        image_url = p["imageInfo"]["thumbnailUrl"]
        price = p["priceInfo"]["priceRange"]["priceString"]
        productList.append(Product(name, store, purchase_url, image_url, price))
    except:
        print("error: failed to load product")


for p in productList:
    print(p)
