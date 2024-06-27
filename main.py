import requests

api_key = "65f400e36d21456eb4e2ca7bba8328a1"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-05-27&sortBy=publishedAt&" \
      "apiKey=65f400e36d21456eb4e2ca7bba8328a1"
# Make request
request = requests.get(url)
# Get dictionary with data
content = request.json()
# Access the article tile and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
