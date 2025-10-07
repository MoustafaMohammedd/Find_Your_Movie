from fastapi import FastAPI
from pydantic import BaseModel

from src.retrieval.search import find_similar_reviews

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    search_method: str = 'mmr'
    n_movies: int = 3
    f_k: int = 10     
 

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Search API"}


    
@app.post("/search")
def search_movies(request: QueryRequest):
    
    user_query = request.query
    search_method = request.search_method
    n_movies = request.n_movies
    f_k = request.f_k
    
    results = find_similar_reviews(user_query, search_method, n_movies, f_k)
    
    return {"results": results}


