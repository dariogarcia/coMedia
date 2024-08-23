import os
import pickle
import xml.etree.ElementTree as ET
from src.content import Content
from src.embedding import embed_contents, store_embedded_contents

def main():
    #This code reads the xml file and produces an embedding of it, storing it in disk
    embedding_model = 'BAAI/bge-m3'
    # Load data and embed each content sample
    tree = ET.parse('data/contents.xml')
    root = tree.getroot()
    contents = []
    for content_element in root.findall("content"):
        content_data = {}
        for child in content_element:
            content_data[child.tag] = child.text
        contents.append(Content(**content_data))
    embedded_contents = embed_contents(contents, embedding_model)
    data_dir = "data"
    output_file_path = os.path.join(data_dir, "embeddings.pkl")
    store_embedded_contents(output_file_path, embedded_contents)
    return

if __name__ == "__main__":
    main()