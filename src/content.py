import xml.etree.ElementTree as ET

class Content:
    def __init__(self, author_id, co_type, description, language, author, date, place, score, link):
        self.author_id = author_id
        self.co_type = co_type
        self.description = description
        self.language = language
        self.author = author
        self.date = date
        self.place = place
        self.score = score
        self.link = link

    def to_xml(self):
        content_elem = ET.Element("content")
        for key, value in self.__dict__.items():
            ET.SubElement(content_elem, key).text = str(value)
        return content_elem

    @classmethod
    def from_xml(cls, xml_elem):
        return cls(
            xml_elem.find("author_id").text,
            xml_elem.find("co_type").text,
            xml_elem.find("description").text,
            xml_elem.find("language").text,
            xml_elem.find("author").text,
            xml_elem.find("date").text,
            xml_elem.find("place").text,
            int(xml_elem.find("score").text),
            xml_elem.find("link").text,
        )
