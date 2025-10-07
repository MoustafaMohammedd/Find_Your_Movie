import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from src.vector_store.load_vector_store import load_vector_store
def get_retriever(search_type='mmr', k=3, fetch_k=10):
    
    reviews_vector_db=load_vector_store(output_path="src/vector_database")

    if search_type == 'mmr':
        retriever = reviews_vector_db.as_retriever(search_type = 'mmr', 
                                            search_kwargs = {'k': 3, 'fetch_k': 10})
    else:
        retriever = reviews_vector_db.as_retriever(search_type = 'similarity', 
                                            search_kwargs = {'k': 3})
        
    return retriever

