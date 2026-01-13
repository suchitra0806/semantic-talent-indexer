from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.llm = Ollama(model="llama3.2", request_timeout=300.0) 
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

def run_search():
    print("🚀 engine is warming up (this might take a minute on the first run)...")
    
    documents = SimpleDirectoryReader("./data").load_data()
    
    index = VectorStoreIndex.from_documents(documents)
    
    query_engine = index.as_query_engine()
    
    print("🔍 ai is generating your summary now...")
    response = query_engine.query("summarize this candidate's experience and technical projects.")

    print(f"\nfinal ai summary:\n{response}")

if __name__ == "__main__":
    run_search()