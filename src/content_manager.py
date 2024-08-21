import os
from scipy.spatial.distance import cosine
from src.content import Content
from src.embedding import embed_query, load_embedded_contents
import xml.etree.ElementTree as ET

class ContentManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contents = []
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            self.contents = [Content.from_xml(content) for content in root.findall("content")]

    def save(self):
        root = ET.Element("contents")
        for content in self.contents:
            root.append(content.to_xml())
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def add_content(self, content):
        self.contents.append(content)
        self.save()

    def search(self, query, llm=False, top_n=3):
        #returns most similar contents to given query
        if llm!=False:
            #LLM embedding based similarity
            emb_query = embed_query(query, llm)
            emb_contents = load_embedded_contents(llm)
            similarities = {}
            for content_desc, content_embedding in emb_contents.items():
                similarity = 1 - cosine(emb_query, content_embedding)
                similarities[content_desc] = similarity
            top_similar = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        else:
            # Text-based similarity
            print('1')
            top_similar = [content.description for content in self.contents if query in content.description]
        return top_similar[:top_n]

    def get_user_contents(self, user_id):
        return [content for content in self.contents if content.author_id == user_id]

