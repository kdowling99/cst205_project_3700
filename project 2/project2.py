'''
Course: CST205-01_FA22
Title: Target Walmart Project
Abstract:
Authors: Christopher Raya, Kyle Dowling, Ricardo Perez JR
Date: 12/05/2022
'''
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask import request
import random
import requests
import json

#API STUFF ~~~~~~~~~~~~~~~~~~~~~~~~~~
#Kyle Dowling worked on all the api stuff

# Class Product stores all the information that we pass to the front end 
# to conveniently reference it in the html using jinga2 magic
class Product:
   ''' a class to model a product '''
   def __init__(self, name, store, purchase_url, image_url, price):
      self.name = name
      self.store = store
      self.purchase_url = purchase_url
      self.image_url = image_url
      self.price = price
   def __str__(self):
      return f'Name: {self.name}\nStore: {self.store}\nPrice: {self.price}'
   def __eq__(self, other):
      return self.purchase_url == other.purchase_url

# this function takes a keyword and then searches both the walmart and target APIS respectfully,
# gathers information about the product results, puts them in the Product class, and finally returns a list of Products
def search_walmart_and_target(keyword):
   productList = []

   # Target API call
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
   
   # Walmart API call
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
# this is how we get flask and the website to work.
#app.route('/') is the start page
#Christopher Raya worked on the front end and flask.
@app.route('/')
def hello():

   return render_template('template.html')

@app.route('/results', methods=['GET'])
def results():
   #This function grabs the products from the api and posts them on the results tab.
   query=request.args.get("query")
   product_list = search_walmart_and_target(query)
   random.shuffle(product_list)
   return render_template('results.html', query=query, product_list=product_list)
