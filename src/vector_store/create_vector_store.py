import faiss
from langchain_community.vectorstores import FAISS 
from langchain_community.document_loaders import DataFrameLoader
from embedding_model import model
import pandas as pd  


def create_vector_store(data_df, model, output_path):
    
    loader = DataFrameLoader(data_df, page_content_column="description")
    descriptions = loader.load()

    reviews_vector_db = FAISS.from_documents(descriptions, model)
    reviews_vector_db.save_local(output_path)
    
    print(f"Vector store created and saved to {output_path}")
    
    
if __name__ == "__main__":


    data_df=pd.read_csv(r"/Find_Your_Movie/data/netflix-tv-shows-and-movies/cleaned_netflix.csv")

    create_vector_store(data_df=data_df, model=model, output_path="src/vector_database")
    