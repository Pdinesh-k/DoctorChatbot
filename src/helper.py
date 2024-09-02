from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def load_pdf(data):
    loader = DirectoryLoader(data,glob = "*.pdf",loader_class=PyPDFLoader)
    file = loader.load()
    return file

def text_split(extracted_data):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap=200)
  text_chunks = text_splitter.split_documents(extracted_data)
  return text_chunks

def embedding_model():
  model_name = "sentence-transformers/all-MiniLM-L6-v2"
  embedding = HuggingFaceEmbeddings(model_name = model_name)
  return embedding
