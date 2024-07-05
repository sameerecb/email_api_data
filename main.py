import requests
from send_email import send_email
api_key = "API_KEY"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-05&sortBy=publishedAt&apiKey=" \
      "<API_KEY"
# Make request
request = requests.get(url)
# Get dictionary with data
content = request.json()
# Access the article tile and description
body = ""
for article in content["articles"]:
    # print(article["title"])  # To print on console
    # print(article["description"])  # To print on console
    if article["title"] is not None:
        if article["description"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"
# print(body)
body = body.encode("utf-8")
send_email(message=body)

