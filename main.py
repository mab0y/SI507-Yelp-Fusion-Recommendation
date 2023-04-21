#########################################
##### Name:                         Boyuan Ma
##### Uniqname:                     boyuanma
#########################################
import json
import requests
import API_KEY
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from flask import Flask,render_template,request

app = Flask(__name__)

# Prompt user to input location to search for businesses
location = input("Please enter your location: ")

# Yelp Fusion API Base URL & API Key
search_url = f"https://api.yelp.com/v3/businesses/search?location={location}&categories=&sort_by=best_match&limit=50"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + API_KEY.KEY
}

# Retrieve and cache Yelp Fusion API data
response = requests.get(search_url, headers=headers)
data = json.loads(response.text)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Define a Business class that saves crucial information derived from Yelp Fusion API JSON
class Business:
    """
    A class representing a business with crucial information derived from JSON.

    Attributes:
    id: The unique ID of the business.
    name: The name of the business.
    image_url: The URL of the business's image.
    url: The URL of the business's Yelp page.
    categories: A list of categories the business belongs to.
    rating: The rating of the business on Yelp.
    location: The street address of the business.
    phone: The phone number of the business.
    reviews: A list of reviews of the business on Yelp.
    """
    def __init__(self,json):
        self.id = json["id"]
        self.name = json["name"]
        self.image_url = json["image_url"]
        self.url = json["url"]
        self.categories = [i["title"] for i in json["categories"]]
        self.rating = json["rating"]
        self.location = json["location"]["address1"]
        self.phone = json["display_phone"]
        self.reviews = []

    # Define the string function of the Business class
    def __str__(self):
        return self.name

# Generate a WordCloud for a given Business
def generate_wordcloud(business):
    """
    Generates a word cloud based on the reviews of a business.

    Parameters:
    business (Business): An instance of the Business class representing a business.

    Returns:
    None
    """
    text = ' '.join(business.reviews)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

     # Save the WordCloud as a PNG image to /static/images folder
    filename = f"{business.id}.png"
    plt.savefig('static/images/'+filename)

# Create a list of Business objects from Yelp Fusion API data
Businesses = [Business(i) for i in data["businesses"]]

# Create a list of Business objects from cached data
f = open("data.json","r")
cache = json.loads(f.read())
Businesses = [Business(i) for i in cache["businesses"]]

# Add reviews to each Business object
for i in Businesses:
    reviews_url = f"https://api.yelp.com/v3/businesses/{i.id}/reviews?limit=50&sort_by=yelp_sort"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_KEY.KEY
    }
    response = requests.get(reviews_url, headers=headers)
    reviews_dic= json.loads(response.text)

    for j in reviews_dic["reviews"]:
        i.reviews.append(j["text"])

# Create a graph by a dictionary of Business categories and their associated Businesses
categories_graph={}
for i in Businesses:
    generate_wordcloud(i)
    for j in i.categories:
        if j not in categories_graph.keys():
            categories_graph[j] = [i]
        else:
            categories_graph[j].append(i)

# Define HTML templates for Flask web pages
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form.get('category')
        filtered_businesses = categories_graph.get(category)
        return render_template('index.html', businesses=filtered_businesses, categories=categories_graph.keys())
    else:
        return render_template('index.html', businesses=Businesses, categories=categories_graph.keys())

@app.route('/wordcloud/<business_id>')
def wordcloud(business_id):
    filename = f"{business_id}.png"
    # Render the wordcloud template and pass in the filename as a variable
    return render_template('wordcloud.html', filename=filename)

# Run the Flask
if __name__ == '__main__':
    print('starting Yelp Fusion Recommendation', app.name)
    app.run(debug=True)