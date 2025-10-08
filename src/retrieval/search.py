import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from relevance_ranking import get_retriever
import pandas as pd



def find_similar_reviews(query,search_method='similarity_score', n_movies=3, f_k=10):
    
    data_df = pd.read_csv(r"data\netflix-tv-shows-and-movies\cleaned_netflix.csv")
    
    retriever = get_retriever(search_type=search_method, n_retrieves=n_movies, n_f_k=f_k)
    
    
    most_similar_reviews = retriever.invoke(query)
    
    results = []
    for doc in most_similar_reviews:
        title = doc.metadata["title"]
        description = data_df[data_df['title'] == title]['description'].iloc[0]
        results.append({"title": title, "description": description})
        
    for i,doc in enumerate(most_similar_reviews):
        print(f"Movie {i+1}:")
        title = doc.metadata["title"]
        print()
        print(f"Title: {title}")
        print()
        print(f"Description: {data_df[data_df['title'] == title]['description'].iloc[0]}")
        print()
        print("-" * 50)
        
        
    return results
if __name__ == "__main__":
    
    user_query = "movie talking about romantic love story between couple fighting to live together"
    results=find_similar_reviews(user_query, search_method='mmr', n_movies=3, f_k=10)
