from bs4 import BeautifulSoup

with open(file="website.html", mode="r", encoding='utf-8') as website:
    contents = website.read()
    print(contents)
