def is_high_imdb(movie):
    return movie.get("imdb", 0) > 5.5

movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}
print(is_high_imdb(movie)) 
