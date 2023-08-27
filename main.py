import requests
import send_mail
import json


api_key = "96c5c5d54a8a4f7880892c4b217d3fe7"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=96c5c5d54a8a4f7880892c4b217d3fe7&" \
      "language=en"

request = requests.get(url)
content = request.json()

#for article in content["articles"]:
#    title = article['title'].encode()
#    description = article['description'].encode()
#
#   send_mail.send_mail(title, description)

body = ""
for article in content["articles"][:10]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["link"] + 2 * "\n"

body = body.encode("utf-8")

send_mail.send_mail("Today's news:", body)
