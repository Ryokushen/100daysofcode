from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.getText()
print(article_text)

article_href = soup.find(name="span", class_="titleline")
article_link = article_href.contents[0].get("href")
print(article_link)

article_score = soup.find(name="span", class_="score")
article_upvote = article_score.getText()
print(article_upvote)


# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())