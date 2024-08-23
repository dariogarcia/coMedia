# coMedia
Storing, indexing and retrieving all sorts of media, using LLM embeddings as backbone.

main.py has three functionalities. Adding content, searching for content (powered by an LLM) and reviewing added content.

The search for content requires existing content to be embedded by an LLM. To do that, embed_main.py processes the xml file and generates the embeddings and stores them in a pkl.
