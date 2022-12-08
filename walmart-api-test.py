import requests

url = "https://walmart.p.rapidapi.com/products/v2/list"

querystring = {"cat_id":"0","sort":"best_seller","page":"1","query":"lamp"}

headers = {
    "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
    "X-RapidAPI-Host": "walmart.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
