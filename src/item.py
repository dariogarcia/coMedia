import xml.etree.ElementTree as ET

class Item:
    def __init__(self, author_id="", item_type="", description="", commentary="", language="", author="", date="", place="", score=0, link="", item_id="", media_id=""):
        self.author_id = author_id
        self.item_type = item_type
        self.description = description
        self.commentary = commentary
        self.language = language
        self.author = author
        self.date = date
        self.place = place
        self.score = score
        self.link = link
        self.item_id = item_id
        self.media_id = media_id
    
    def to_xml(self):
        item_elem = ET.Element("item")
        for key, value in self.__dict__.items():
            ET.SubElement(item_elem, key).text = str(value)
        return item_elem

    @classmethod
    def from_xml(cls, xml_elem):
        author_id = xml_elem.find("author_id")
        item_type = xml_elem.find("item_type")
        description = xml_elem.find("description")
        commentary = xml_elem.find("commentary")
        language = xml_elem.find("language")
        author = xml_elem.find("author")
        date = xml_elem.find("date")
        place = xml_elem.find("place")
        score = xml_elem.find("score")
        link = xml_elem.find("link")
        item_id = xml_elem.find("item_id")
        media_id = xml_elem.find("media_id")
        return cls(
            author_id.text if author_id is not None else None,
            item_type.text if item_type is not None else None,
            description.text if description is not None else None,
            commentary.text if commentary is not None else None,
            language.text if language is not None else None,
            author.text if author is not None else None,
            date.text if date is not None else None,
            place.text if place is not None else None,
            int(score.text) if score is not None else 0,
            link.text if link is not None else None,
            item_id.text if item_id is not None else None,
            media_id.text if media_id is not None else None,
        )
