import requests

api_key = "Enter API KEY"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-05-27&sortBy=publishedAt&" \
      "apiKey=Enter API Key"
# Make request
request = requests.get(url)
# Get dictionary with data
content = request.json()
# Access the article tile and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
