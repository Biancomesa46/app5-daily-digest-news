import requests

api_key = "96c5c5d54a8a4f7880892c4b217d3fe7"

url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=96c5c5d54a8a4f7880892c4b217d3fe7"

request = requests.get(url)
content = request.text
print(content)