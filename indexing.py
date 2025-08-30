from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_core.embeddings import Embeddings
from typing import List

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            response = genai.embed_content(
                model="models/embedding-001",
                content=text
            )
            embeddings.append(response["embedding"])
        return embeddings
    
    def embed_query(self, text: str) -> List[float]:
        response = genai.embed_content(
            model="models/embedding-001",
            content=text
        )
        return response["embedding"]

def run_indexing(uploaded_pdf_path):
    loader=PyPDFLoader(file_path=uploaded_pdf_path)
    doc=loader.load()    # pdf read

    # chunking
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    split_doc = text_splitter.split_documents(documents=doc)

    # Create Gemini embeddings instance
    embeddings = GeminiEmbeddings()

    # vector database
    vector_store = QdrantVectorStore.from_documents(
        documents=split_doc,
        url="http://localhost:6333",
        collection_name="Learning_vectors",
        embedding=embeddings,
        force_recreate=True
    )
    







