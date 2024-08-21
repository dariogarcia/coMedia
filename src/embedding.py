import os
import torch
from transformers import AutoTokenizer, AutoModel

def embed_query(query, model_name):
    #Given an XML contents structure and an embedding model
    #Embed the contents description field using the model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    inputs = tokenizer(query, return_tensors="pt").to(device)
    outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding

def embed_contents(contents, model_name):
    #Given an XML contents structure and an embedding model
    #Embed the contents description field using the model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    embedded_contents = {}
    for content in contents:
        inputs = tokenizer(content.description, return_tensors="pt").to(device)
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
        embedded_contents[content] = embedding
    return embedded_contents

def load_embedded_contents(embedding_model):
    #Given an embedding model, load a file with the contents embedded by it
    #and return those in a dict
    data_dir = "data"
    output_file_path = os.path.join(data_dir, f"{embedding_model}_embeddings.txt")
    if os.path.exists(output_file_path) == False:
        print("Embedding file missing. Aborting.")
        return
    embedded_contents = {}
    with open(output_file_path, "r") as f:
        for line in f:
            content_desc, embedding_str = line.strip().split("\t")
            embedding = [float(x) for x in embedding_str.split(",")]
            embedded_contents[content_desc] = embedding