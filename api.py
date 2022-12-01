import requests
import json
def json_print(response):
    j = json.loads(response.text)
    print(json.dumps(j,indent=2))

def search_walmart_and_target(keyword):
    url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/product/search"

    querystring = {"store_id":"2306","keyword":keyword,"offset":"0","limit":"24","sponsored":"1","rating":"0"}

    headers = {
        "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
        "X-RapidAPI-Host": "target-com-store-product-reviews-locations-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_print(response)


    url = "https://walmart.p.rapidapi.com/v2/auto-complete"

    querystring = {"term":keyword}

    headers = {
        "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
        "X-RapidAPI-Host": "walmart.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_print(response)


print("Enter keyword to search: ")
search_walmart_and_target(input())