import os
from src.content import Content
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

    def search(self, query):
        # Simple text-based search for now
        results = [content for content in self.contents if query in content.description]
        return results

    def get_user_contents(self, user_id):
        return [content for content in self.contents if content.author_id == user_id]

