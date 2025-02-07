#Write a function that returns a sublist of movies with an IMDB score above 5.5
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
]

print(high_rated_movies(movies))
"""[
{'name': 'Hitman', 'imdb': 6.3, 'category': 'Action'},
{'name': 'Dark Knight', 'imdb': 9.0, 'category': 'Adventure'}
]"""
