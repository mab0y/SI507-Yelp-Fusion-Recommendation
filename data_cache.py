import json
import requests
import API_KEY
#Base url & API Key
url = "https://api.yelp.com/v3/businesses/search?location=ann%20arbor&categories=&sort_by=best_match&limit=50"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + API_KEY.KEY
}

#Retrieve and cache data
response = requests.get(url, headers=headers)
data = json.loads(response.text)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#Business class that take crucial information
class Business:
    def __init__(self,json):
        self.name = json["name"]
        self.image_url = json["image_url"]
        self.url = json["url"]
        self.categories = [i["title"] for i in json["categories"]]
        self.rating = json["rating"]
        self.location = json["location"]["address1"]
        self.phone = json["display_phone"]
    def __str__(self):
        return self.name

#Build class without cached data
Businesses = [Business(i) for i in data["businesses"]]

#Build class with cached data
f = open("data.json","r")
cache = json.loads(f.read())
Businesses = [Business(i) for i in cache["businesses"]]

#Build graph
categories_graph={}
for i in Businesses:
    for j in i.categories:
        if j not in categories_graph.keys():
            categories_graph[j] = [i]
        else:
            categories_graph[j].append(i)

print(categories_graph)
