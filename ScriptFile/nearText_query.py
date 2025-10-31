import weaviate
from weaviate.classes.init import Auth
import os, json

# Best practice: store your credentials in environment variables
weaviate_url = "tckttuhrgmctgl2haqnka.c0.europe-west3.gcp.weaviate.cloud"
weaviate_api_key = "MXNDOURpMnUyM2svZ0hwVF92eTcyRXVnaEVORTVvYzZqOHJ5OXhGNDIzdy9wVW00Q3RNaHk4eS9oWXJnPV92MjAw"

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(weaviate_api_key),             # Replace with your Weaviate Cloud key
)

questions = client.collections.use("Note")

response = questions.query.near_text(
    query=input("enter the name of the note: "),
    limit=1
)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()  # Free up resources