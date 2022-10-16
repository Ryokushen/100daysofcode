from bs4 import BeautifulSoup
# import lxml

# Open website as a readable object
with open(file="website.html", mode="r") as website:
    contents = website.read()

# Import bs4 module and pass readable object and parser
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)

# Can use prettify to view HTML structure
# print(soup.prettify())

# Use find_all fxn to find all occurrences of a tag
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.get("href"))
#     # print(tag.getText())
#     pass

# Find individual heading with class
heading = soup.find(name="h1", id="name")
print(heading)