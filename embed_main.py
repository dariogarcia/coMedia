import os
import pickle
import xml.etree.ElementTree as ET
from src.item import Item
from src.embedding import embed_items, store_embedded_items

def main():
    #This code reads the xml file and produces an embedding of all items within it, storing them in disk
    embedding_model = 'BAAI/bge-m3'
    tree = ET.parse('data/items.xml')
    root = tree.getroot()
    items = []
    for item_element in root.findall("item"):
        item_data = {}
        for child in item_element:
            item_data[child.tag] = child.text
        items.append(Item(**item_data))
    embedded_items = embed_items(items, embedding_model)
    data_dir = "data"
    output_file_path = os.path.join(data_dir, "embeddings.pkl")
    store_embedded_items(output_file_path, embedded_items)
    return

if __name__ == "__main__":
    main()