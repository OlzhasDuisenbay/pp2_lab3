#Write a function that takes a category and computes the average IMDB score.
def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]

    if not category_movies:
        return 0

    total_score = 0
    for movie in category_movies:
        total_score += movie["imdb"]

    return total_score / len(category_movies)

movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
]

print(average_imdb_by_category(movies, "Romance"))
#6.8
