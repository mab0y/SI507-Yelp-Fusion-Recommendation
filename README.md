# SI507-Yelp-Fusion-Recommendation

This is a web application that utilizes the Yelp Fusion API to provide restaurant recommendations based on location and category. The app retrieves data from Yelp API, caches it locally, and processes it to generate word clouds for each business. Users can view the word clouds and filter the businesses based on categories.

## Prerequisites

- Python 3.x
- Yelp Fusion API key
- Required Python packages: requests, json, wordcloud, matplotlib, flask

## Data Structure
The application utilizes a graph data structure to represent the categories of the businesses. The graph is implemented using a dictionary in the main.py file, where each key is a category and the value is a set of businesses that belong to that category. When the user selects a category from the drop-down menu, the application retrieves the businesses belonging to that category from the graph and displays them to the user.

## Usage

1. Obtain a Yelp Fusion API key from https://www.yelp.com/developers.
2. Open API_KEY.py and replace YOUR_API_KEY with your actual API key.
3. Run the app.py script: `python main.py`.
4. Access the web application in your web browser at http://localhost:5000/.
5. Enter a location to retrieve recommendations from Yelp Fusion API.
6. Filter the businesses based on categories by selecting a category from the drop-down menu and clicking "Filter".
7. View the word cloud of a business by clicking "View Wordcloud" next to the business name.
