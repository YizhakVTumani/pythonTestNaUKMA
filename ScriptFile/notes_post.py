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
dict = [{"Name": input("Enter a name of a note: "), "Text": input("Enter your note: ")}]
print (dict)

data = dict

questions = client.collections.use("Note")

with questions.batch.fixed_size(batch_size=200) as batch:
    for d in data:
        batch.add_object(
            {
                "name": d["Name"],
                "text": d["Text"],
            }
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = questions.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

client.close()  # Free up resources



