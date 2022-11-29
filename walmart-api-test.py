import requests

url = "https://walmart.p.rapidapi.com/v2/auto-complete"

querystring = {"term":"macbook air"}

headers = {
    "X-RapidAPI-Key": "59bf78a120msh202ae2ddf319bffp1ade43jsn475905aa75be",
    "X-RapidAPI-Host": "walmart.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
