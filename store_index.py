from src.helper import load_pdf,text_split,embedding_model
import os
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

extracted_data = load_pdf("../data/")
text_chunks = text_split(extracted_data)
embeddings = embedding_model()

def vector_embedding():
  store = FAISS.from_documents(text_chunks,embeddings)
  embedding = store.as_retriever()
  return embedding
vector_database = vector_embedding()

