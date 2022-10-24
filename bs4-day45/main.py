from bs4 import BeautifulSoup
# import lxml (Different parser)

with open(file="website.html", mode="r", encoding='utf-8') as website:
    contents = website.read()
   

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print(soup.prettify)

print(soup.a)
