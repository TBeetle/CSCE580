import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# Written by Tyler Beetle

url='/Users/tylerbeetle/Desktop/CSCE581/CLEANED_recipes.csv'
df = pd.read_csv(url)

tfidf = TfidfVectorizer(stop_words="english")
df['ingredients'] = df['ingredients'].fillna('')
df['tags'] = df['tags'].fillna('')
df['combined'] = df['ingredients']+''+df['tags']
tfidf_matrix = tfidf.fit_transform(df['combined'])

cosin_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(query, cosin_sim = cosin_sim):
     # Transform the query using the vectorizer
    query_vector = tfidf.transform([query])

    # Calculate the cosine similarity between the query and the data
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()

    # Get the indices of the most similar items
    sim_scores = list(enumerate(cosine_similarities))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]

    sim_indices = [i[0] for i in sim_scores]

    # Print the recommendations
    #print(df["name"].iloc[sim_indices])
    recommendations = df["name"].iloc[sim_indices].reset_index(drop=True)
    formatted_recommendations = "\n".join([f"{i+1}. {name}" for i, name in enumerate(recommendations)])
    print(formatted_recommendations)
    return recommendations

def get_recipe_info(query):
     # Check if the recipe name is in the dataframe
    print("Recipe Selection:", query)
    if query in df["name"].values:
        index = df[df["name"] == query].index[0]
        description = df["description"].iloc[index]
        ingredients = df["ingredients"].iloc[index]
        directions = df["steps"].iloc[index]
        print("description:", description)
        print("ingredients: ", ingredients)
        print("directions: ", directions)
    else:
        print("Information not found")
    

def get_recipe_description(recipe_index, df):
    return df.at[recipe_index, 'description']