import chromadb
from chromadb.config import Settings
CHROMA_PATH = "chroma"
# Initialize ChromaDB client
client = chromadb.Client(Settings(persist_directory=CHROMA_PATH))
collections = client.list_collections()
print(collections)
# Get the collection by name
# collection_name = "my_collection"
# collection = client.get_collection(collection_name)

# # Delete all entries in the collection
# collection.delete()  # This clears all data in the collection
