import os
from scipy.spatial.distance import cosine
from src.item import Item
from src.embedding import embed_query, load_embedded_items
import xml.etree.ElementTree as ET

def get_next_item_id(item_manager):
    existing_ids = set()
    for item in item_manager.items:
      existing_ids.add(item.item_id)
    next_id = 1
    while next_id in existing_ids:
      next_id += 1
    return next_id

class ItemManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = []
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            self.items = [Item.from_xml(item) for item in root.findall("item")]

    def save(self):
        root = ET.Element("items")
        for item in self.items:
            root.append(item.to_xml())
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def add_item(self, item):
        self.items.append(item)
        self.save()

    def associate_content(self, description, llm="BAAI/bge-m3", top_n=3):
        #Finds the most likely content for a given commentary. If none, creates one based on it.
        #TODO: Add optional fields as inputs to improve matchmaking
        top_similar_items = self.retrieve_by_similarity(description, match_comm_comm=False, match_cont_desc=True)
        for item in top_similar_items:
            response = input("Is this content the one?\n"+item[0]+"\n (Y/N)")
            if response=='Y':
                return item[1][0]
        #if it reaches here, none was found. create new one
        item_id = get_next_item_id(self)
        self.items.append(Item(author_id="", item_type="content", description=description, commentary="", language="", author="", date="", place="", score=0, link="", item_id=item_id, media_id=""))
        self.save()
        return item_id

    def retrieve_by_similarity(self, query, match_cont_desc, match_comm_comm, llm="BAAI/bge-m3", top_n=3):
        #returns most similar items to given query. Matches either the content description or the comments comment.
        if (match_comm_comm and match_cont_desc) or (not match_comm_comm and not match_cont_desc):
            raise ValueError("Exactly one of match_cont_desc and match_comm_comm must be True.")
        emb_query = embed_query(query)
        embedded_items = load_embedded_items()
        similarities = {}
        for item_id, item_value in embedded_items.items():
            if match_cont_desc:
                if item_value[0]=="commentary":
                    continue
                similarity = 1 - cosine(emb_query, item_value[1][1])
                similarities[item_value[1][0]] = (item_id,similarity)
            else:#match_comm_comm
                if item_value[0]=="content":
                    continue
                similarity = 1 - cosine(emb_query, item_value[2][1])
                similarities[item_value[2][0]] = (item_id,similarity)
        top_similar = sorted(similarities.items(), key=lambda x: x[1][1], reverse=True)
        return top_similar[:top_n]

    def get_user_items(self, user_id):
        return [item for item in self.items if item.author_id == user_id]

