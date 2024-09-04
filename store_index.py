from src.helper import load_pdf,text_split,embedding_model
import os
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

def vector_embedding():
  if os.path.exists("faiss_index"):
    store = FAISS.load_local("faiss_index",embedding_model())
    print("Loaded existing FAISS index")
  else:
    extracted_data = load_pdf("../data/")
    text_chunks = text_split(extracted_data)
    embeddings = embedding_model()
    store = FAISS.from_documents(text_chunks,embeddings)
    store.save_local("faiss_index")
    print("Created and saved a new FAISS index.")
    embedding = store.as_retreiver()
    return embedding

vector_database = vector_embedding()

