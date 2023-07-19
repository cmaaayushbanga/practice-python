import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-06-19&sortBy=publishedAt&apiKey=5f8e698b2449447180e20575f3d8b0f5"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")