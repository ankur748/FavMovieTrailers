import fresh_tomatoes
import movie

import csv

movies = []

#movies.txt will be used to store data for movies. File be read here and fetched to fresh_tomatoes module for html generation
with open('movies.txt', 'rb') as movie_file:
    movie_reader = csv.reader(movie_file)
    for row in movie_reader:

        title               = row[0]
        poster_image_url    = row[1]
        trailer_youtube_url = row[2]

        new_movie = movie.Movie(title,poster_image_url,trailer_youtube_url)

        movies.append(new_movie)

fresh_tomatoes.open_movies_page(movies)
