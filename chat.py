from langchain_qdrant import QdrantVectorStore
import google.generativeai as genai
import os
from dotenv import load_dotenv
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
def chat_with_pdf(query):
    # Create Gemini embeddings instance
    embeddings = GeminiEmbeddings()
    
    # vector database
    vector_db = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="Learning_vectors",
        embedding=embeddings
    )

    # vector search in existing database
    search_results = vector_db.similarity_search(
        query=query,
        k=3  # Limit to top 3 results
    )

    print(f"Found {len(search_results)} relevant documents")

    # Create context from search results
    context = "\n\n".join([
        f"Page Number: {result.metadata.get('page', 'N/A')}\n"
        f"File Location: {result.metadata.get('source', 'N/A')}\n"
        f"Page Content:\n{result.page_content}"
        for result in search_results
    ])

    system_prompt = f"""
    You are an intelligent AI agent.
    You give answers to user queries with page numbers and answer them beautifully.

    You should only answer user query based on the provided context and also navigate user to page number to know more.

    Context:
    {context}

    User Question: {query}

    Please provide a helpful answer with page references:
    """

    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(
        system_prompt + "\n\n" + query
    )
    return response.text
