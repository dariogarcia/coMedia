import os
import pickle
from FlagEmbedding import BGEM3FlagModel
import warnings
#TODO fix this
warnings.filterwarnings("ignore", category=FutureWarning, module="FlagEmbedding")

def embed_query(query, model_name="BAAI/bge-m3"):
    model = BGEM3FlagModel(model_name)
    embedding = model.encode(query, batch_size=1, max_length=8192)['dense_vecs']
    return embedding

def embed_items(items, model_name="BAAI/bge-m3"):
    #produces a dictionary of all contents, with co_ids as keys, and a tuple of tuples as values
    #tuples include type[0], description[1][0] and embedding[1][0], commentary[2][0] and embedding[2][1]
    model = BGEM3FlagModel(model_name)
    embedded_items = {}
    for item in items:
        embedding_desc = model.encode(item.description, batch_size=12, max_length=8192)['dense_vecs']
        embedding_comm = model.encode(item.commentary, batch_size=12, max_length=8192)['dense_vecs']
        embedded_items[item.item_id] = (item.item_type,(item.description,embedding_desc),(item.commentary,embedding_comm))
    return embedded_items

def load_embedded_items():
    # Construct the output file path
    data_dir = "data"
    output_file_path = os.path.join(data_dir, "embeddings.pkl")
    if os.path.exists(output_file_path):
        # Load the embedded items from the pickle file
        with open(output_file_path, "rb") as f:
            embedded_items = pickle.load(f)
        return embedded_items
    else:
        print("Embedding file missing. Aborting.")
        return None

def store_embedded_items(output_file_path, embedded_items):
    if os.path.exists(output_file_path):
        overwrite = input(f"Output file {output_file_path} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            print("Aborting.")
            return
    with open(output_file_path, "wb") as f:
        pickle.dump(embedded_items, f)
    print("Embeddings saved to", output_file_path)
    return