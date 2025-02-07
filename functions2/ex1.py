"""Write a function that takes a single movie and returns True if its
IMDB score is above 5.5"""
def is_high_rated(movie):
    return movie["imdb"] > 5.5

movie = {"name": "Hitman", "imdb": 6.3, "category": "Action"}
print(is_high_rated(movie))
#True
