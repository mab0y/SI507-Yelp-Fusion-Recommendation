# SI507-Yelp-Fusion-Recommendation

This is a web application that utilizes the Yelp Fusion API to provide restaurant recommendations based on location and category. The app retrieves data from Yelp API, caches it locally, and processes it to generate word clouds for each business. Users can view the word clouds and filter the businesses based on categories.

## Prerequisites

- Python 3.x
- Yelp Fusion API key
- Required Python packages: requests, json, wordcloud, matplotlib, flask

## Usage

1. Obtain a Yelp Fusion API key from https://www.yelp.com/developers.
2. Open API_KEY.py and replace YOUR_API_KEY with your actual API key.
3. Run the app.py script: `python main.py`.
4. Access the web application in your web browser at http://localhost:5000/.
5. Enter a location to retrieve recommendations from Yelp Fusion API.
6. Filter the businesses based on categories by selecting a category from the drop-down menu and clicking "Filter".
7. View the word cloud of a business by clicking "View Wordcloud" next to the business name.

## Credits

- This project is built with Flask, a Python web framework.
- The Yelp Fusion API is provided by Yelp.
- The wordcloud generation is powered by the wordcloud package.
- The application uses the Matplotlib library for generating and displaying plots.
- The HTML templates are based on the Flask framework.
