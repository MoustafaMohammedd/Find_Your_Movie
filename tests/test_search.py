import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.retrieval.search import find_similar_reviews



user_query = "movie talking about romantic love story between couple fighting to live together"
results=find_similar_reviews(user_query, search_method='mmr', n_movies=3, f_k=10)