from bs4 import BeautifulSoup
import requests

playlist_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
music_pull = requests.get(f"https://www.billboard.com/charts/hot-100/{playlist_date}")
music_pull.raise_for_status()
soup_mix = music_pull.text



soup = BeautifulSoup(soup_mix, "html.parser")
# fresh_soup = soup.prettify()

songs_name = soup.select("h3.c-title.a-no-trucate")
song = [song.get_text().strip() for song in songs_name]
artist_name = soup.select("span.c-label.a-no-trucate")
artist = [artist.get_text().strip() for artist in artist_name]





print(song)
print(artist)
