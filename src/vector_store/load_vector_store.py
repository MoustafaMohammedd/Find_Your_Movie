import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from embedding_model import model
from langchain_community.vectorstores import FAISS



def load_vector_store(output_path="src/vector_database"):
    reviews_vector_db = FAISS.load_local(
        output_path, model,allow_dangerous_deserialization=True)
    
    return reviews_vector_db