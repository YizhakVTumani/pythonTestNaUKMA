import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure
import os

# Best practice: store your credentials in environment variables
weaviate_url = "tckttuhrgmctgl2haqnka.c0.europe-west3.gcp.weaviate.cloud"
weaviate_api_key = "MXNDOURpMnUyM2svZ0hwVF92eTcyRXVnaEVORTVvYzZqOHJ5OXhGNDIzdy9wVW00Q3RNaHk4eS9oWXJnPV92MjAw"

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,  # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(weaviate_api_key),  # Replace with your Weaviate Cloud key
)

questions = client.collections.create(
    name="Note",
    vector_config=Configure.Vectors.text2vec_weaviate(),  # Configure the Weaviate Embeddings integration
)

client.close()  # Free up resources

# RestEndPoint = tckttuhrgmctgl2haqnka.c0.europe-west3.gcp.weaviate.cloud
# gRPC = grpc-tckttuhrgmctgl2haqnka.c0.europe-west3.gcp.weaviate.cloud
# API = MXNDOURpMnUyM2svZ0hwVF92eTcyRXVnaEVORTVvYzZqOHJ5OXhGNDIzdy9wVW00Q3RNaHk4eS9oWXJnPV92MjAw