import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Получаем HTML-код страницы
response = requests.get(URL)
website_html = response.text

# Создаем объект BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Находим все заголовки фильмов
all_movies = soup.find_all(name="h3", class_="title")

# Извлекаем текст заголовков фильмов
movie_titles = [movie.getText() for movie in all_movies]
# Реверсируем список фильмов
movies = movie_titles[::-1]

# Записываем фильмы в файл с кодировкой UTF-8
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
