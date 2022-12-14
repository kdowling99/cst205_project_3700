from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask import request
import random
import requests
import json

#API STUFF ~~~~~~~~~~~~~~~~~~~~~~~~~~
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
	"X-RapidAPI-Key": "6522102ca0msh755bfb68d625a1bp16e2f2jsnd67d6bb895dd",
	"X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
   }
   response = requests.request("GET", url, headers=headers, params=querystring)
   print(response.text)
   j = json.loads(response.text)
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
   url = "https://walmart.p.rapidapi.com/products/v2/list"
   querystring = {"cat_id":"0","sort":"best_seller","page":"1","query":keyword}
   headers = {
      "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
      "X-RapidAPI-Host": "walmart.p.rapidapi.com"
   }
   response = requests.request("GET", url, headers=headers, params=querystring)
   print(response.text)
   j = json.loads(response.text)
   for x in range(0,5):
    try:
        p = j["data"]["search"]["searchResult"]["itemStacks"][0]["items"][x]
        name = p["name"]
        store = "Walmart"
        purchase_url = "https://www.walmart.com" + p["canonicalUrl"]
        image_url = p["imageInfo"]["thumbnailUrl"]
        price = p["priceInfo"]["priceRange"]["priceString"]
        productList.append(Product(name, store, purchase_url, image_url, price))
    except:
        print("error: failed to load product")
   return productList

#END API STUFF ~~~~~~~~~~~~~~~~~~~~~~



app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():

   return render_template('template.html')

@app.route('/results', methods=['GET'])
def results():
   query=request.args.get("query")
   product_list = search_walmart_and_target(query)
   random.shuffle(product_list)
   return render_template('results.html', query=query, product_list=product_list)
