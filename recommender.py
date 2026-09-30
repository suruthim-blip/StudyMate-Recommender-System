import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load the dataset
data = pd.read_csv("dataset.csv")


# Combine important columns for recommendation
data["features"] = (
    data["subject"].astype(str) + " " +
    data["difficulty"].astype(str) + " " +
    data["category"].astype(str) + " " +
    data["description"].astype(str)
)


# Convert text into numerical vectors
vectorizer = TfidfVectorizer()
feature_matrix = vectorizer.fit_transform(data["features"])


# Calculate similarity between resources
similarity_matrix = cosine_similarity(feature_matrix)


def recommend_resources(subject, difficulty, top_n=5):
    """
    Recommend study resources based on subject and difficulty.
    """

    query = subject + " " + difficulty

    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(
        query_vector,
        feature_matrix
    ).flatten()

    # Get highest similarity indexes
    recommended_indices = similarity_scores.argsort()[-top_n:][::-1]

    recommendations = data.iloc[recommended_indices]

    return recommendations[
        ["title", "subject", "difficulty", "resource_type", "description"]
    ]


# Test the recommendation system
if __name__ == "__main__":

    subject = input("Enter the subject: ")
    difficulty = input("Enter difficulty level (Beginner/Intermediate/Advanced): ")

    results = recommend_resources(subject, difficulty)

    print("\nRecommended Study Resources:\n")
    print(results.to_string(index=False))
