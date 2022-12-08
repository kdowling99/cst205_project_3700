import requests
import json

def keyRecurse(d):
    for x in d:
        print(x)
        keyRecurse(d[x])

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

def search_walmart_and_target(keyword):
    productList = []

    url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/product/search"
    querystring = {"store_id":"2306","keyword":keyword,"offset":"0","limit":"24","sponsored":"1","rating":"0"}
    headers = {
        "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
        "X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    j = json.loads(response.text)
    # print(j)
    #print(json.dumps(j["products"]))
    # for x in range(0,5):
    #     p = j["products"][x]
    #     name = p["item"]["product_description"]["title"]
    #     store = "Target"
    #     purchase_url = p["item"]["enrichment"]["buy_url"]
    #     image_url = p["item"]["enrichment"]["images"]["primary_image_url"]
    #     price = p["price"]["formatted_current_price"]
    #     productList.append(Product(name, store, purchase_url, image_url, price))
    #keyRecurse(j)

    url = "https://walmart.p.rapidapi.com/products/v2/list"
    querystring = {"cat_id":"0","sort":"best_seller","page":"1","query":keyword}
    headers = {
        "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
        "X-RapidAPI-Host": "walmart.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    j = json.loads(response.text)
    # print(json.dumps(j["data"]["search"]["searchResult"]["itemStacks"][0]["items"]))
    #for p in j["data"]["search"]["searchResult"]["itemStacks"][0]["items"]:
    # for x in range(0,5):
    #     p = j["data"]["search"]["searchResult"]["itemStacks"][0]["items"][x]
    #     name = p["name"]
    #     store = "Walmart"
    #     purchase_url = "www.walmart.com" + p["canonicalUrl"]
    #     image_url = p["imageInfo"]["thumbnailUrl"]
    #     price = p["priceInfo"]["priceRange"]["priceString"]
    #     productList.append(Product(name, store, purchase_url, image_url))

    return productList

print("Enter keyword to search: ")
productList = search_walmart_and_target(input())

for p in productList:
    print(p)