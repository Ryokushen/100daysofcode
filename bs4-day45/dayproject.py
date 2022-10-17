from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/"
                            "https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
for movies in movie_titles:
    print(movies.getText())
