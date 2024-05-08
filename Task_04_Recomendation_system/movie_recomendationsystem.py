class SimpleRecommendationSystem:
    def __init__(self, items):
        self.items = items

    def recommend(self, user_preferences):
        recommended_items = []
        for item, genres in self.items.items():
            if any(genre in user_preferences for genre in genres):
                recommended_items.append(item)
        return recommended_items


# Sample data: movies and their genres
movies = {
    "The Shawshank Redemption": ["drama"],
    "The Godfather": ["drama", "crime"],
    "The Dark Knight": ["action", "crime", "drama"],
    "Pulp Fiction": ["crime", "drama"],
    "Forrest Gump": ["drama", "romance"],
    "Inception": ["action", "adventure", "sci-fi"]
}

# Create recommendation system
recommendation_system = SimpleRecommendationSystem(movies)

# User preferences
user_preferences = ["drama", "crime"]

# Get recommendations
recommendations = recommendation_system.recommend(user_preferences)
print("Recommended movies:")
for movie in recommendations:
    print("-", movie)
