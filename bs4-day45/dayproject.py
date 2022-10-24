from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/"
                            "https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

movie_list = []
movie_titles = soup.find_all(name="h3", class_="title")
for movies in movie_titles:
    movienum = movies.getText()
    movie_list.append(movienum)

movie_list.reverse()
print(movie_list)
for movie in movie_list:
    with open("movie-list.txt", "a") as file:
        file.write(movie)
        file.write("\n")