"""Write a function that takes a category name and
returns just those moviesunder that category"""
def movies_by_category(movies, category):
    result = []
    for movie in movies:
        if movie["category"].lower() == category.lower():
            result.append(movie)
    return result

movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
]

print(movies_by_category(movies, "Romance"))
"""[{'name': 'The Choice', 'imdb': 6.2, 'category': 'Romance'}, {'name': 'Colonia', 'imdb': 7.4, 'category': 'Romance'}]"""

