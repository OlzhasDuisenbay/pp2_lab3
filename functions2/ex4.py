#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies):
    if not movies:
        return 0

    total_score = 0
    for movie in movies:
        total_score += movie["imdb"]

    return total_score / len(movies)

# Example usage:
movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
]

print(average_imdb_score(movies))
# 7.225
