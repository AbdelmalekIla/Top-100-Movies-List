import requests
from bs4 import BeautifulSoup
from pprint import pprint
data = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                    "-movies-2/")
html_data = data.text

soup = BeautifulSoup(html_data, 'html.parser')
movie_list = soup.find_all(name="h3", class_="title")
all_movies = [(movie.getText().replace("â\x80\x93", "-")) for movie in movie_list]
top_100_movie = all_movies[::-1]
with open("top_100_movie.txt", "w") as file:
    for i in top_100_movie:
        file.write(f"{i}\n")





