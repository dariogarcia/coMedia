import os
import pickle
from FlagEmbedding import BGEM3FlagModel

def embed_query(query, model_name="BAAI/bge-m3"):
    model = BGEM3FlagModel(model_name)
    embedding = model.encode(query, batch_size=1, max_length=8192)['dense_vecs']
    return embedding

def embed_contents(contents, model_name="BAAI/bge-m3"):
    model = BGEM3FlagModel(model_name)
    embedded_contents = {}
    for content in contents:
        embedding = model.encode(content.description, batch_size=12, max_length=8192)['dense_vecs']
        embedded_contents[content.description] = embedding
    return embedded_contents

def load_embedded_contents(embedding_model):
    # Construct the output file path
    data_dir = "data"
    output_file_path = os.path.join(data_dir, "embeddings.pkl")
    if os.path.exists(output_file_path):
        # Load the embedded contents from the pickle file
        with open(output_file_path, "rb") as f:
            embedded_contents = pickle.load(f)
        return embedded_contents
    else:
        print("Embedding file missing. Aborting.")
        return None

def store_embedded_contents(output_file_path, embedded_contents):
    if os.path.exists(output_file_path):
        overwrite = input(f"Output file {output_file_path} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            print("Aborting.")
            return
    with open(output_file_path, "wb") as f:
        pickle.dump(embedded_contents, f)
    print("Embeddings saved to", output_file_path)
    return