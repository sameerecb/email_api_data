import requests
from send_email import send_email
topic = "tesla"
api_key = "65f400e36d21456eb4e2ca7bba8328a1"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-06-05" \
      "&sortBy=publishedAt&" \
      "apiKey=65f400e36d21456eb4e2ca7bba8328a1&" \
      "language=en"
# Make request
request = requests.get(url)
# Get dictionary with data
content = request.json()
# Access the article tile and description
body = ""
for article in content["articles"][:20]:
    # print(article["title"])  # To print on console
    # print(article["description"])  # To print on console
    if article["title"] is not None:
        if article["description"] is not None:
            body = "Subject: Today's News" + "\n" \
                   + body + article["title"] + "\n" + \
                   article["description"] + "\n" + \
                   article["url"] + 2*"\n"
# print(body)
body = body.encode("utf-8")
send_email(message=body)

