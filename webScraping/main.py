import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


movies = soup.find_all('h3', class_='title')
moviesList = []


for movie in movies:
    moviesList.append(movie.text)

movies = moviesList.reverse()

file = open('movies.txt', 'w')
for movie in moviesList:
    file.write(movie+'\n')

file.close()
