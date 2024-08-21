import argparse
import os
import xml.etree.ElementTree as ET
from src.content import Content
from src.embedding import embed_contents

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_file", help="Path to the XML file")
    parser.add_argument("embedding_model", help="Hugging Face model name")
    args = parser.parse_args()
    # Load XML data
    tree = ET.parse(args.xml_file)
    root = tree.getroot()
    # Create Content objects and embed descriptions
    contents = [Content(content) for content in root.findall("content")]
    embedded_contents = embed_contents(contents, args.embedding_model)
    # Construct the output file path
    data_dir = "data"
    output_file_path = os.path.join(data_dir, f"{args.embedding_model}_embeddings.txt")
    # Check file and overwriting
    if os.path.exists(output_file_path):
        overwrite = input(f"Output file {output_file_path} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            print("Aborting.")
            return
    with open(output_file_path, "w") as f:
        for content, embedding in embedded_contents.items():
            f.write(f"{content.description}\t{embedding}\n")

if __name__ == "__main__":
    main()
