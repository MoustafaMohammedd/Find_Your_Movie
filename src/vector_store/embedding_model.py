from langchain.embeddings import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv(".env")
import os


model_name=os.getenv("MODEL_NAME")

model = HuggingFaceEmbeddings(model_name=model_name)