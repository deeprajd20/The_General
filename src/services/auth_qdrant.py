from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from dotenv import load_dotenv
import os
load_dotenv()
qdrant_api_key = os.getenv('qdrant_cloud') 

qdrant_client = QdrantClient(
    url="https://b49a8ab5-2992-4abe-bb76-e4a1a9a73b6e.europe-west3-0.gcp.cloud.qdrant.io:6333", 
    api_key=qdrant_api_key,
)

qdrant_client.recreate_collection(collection_name="chats_db",
                                  vectors_config=VectorParams(size=768,
                                                            distance = Distance.COSINE),
                                  on_disk_payload=True)


