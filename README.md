# coMedia

This project has two purposes. First, to provide a personal repository of appreciated content. One where you can store all that we read, watch, listen to, and care to remember in the future. A sort of second brain. Ssecond, to create a universal, collaborative database of quality consumer media, encoded in a way that allows high expressive queries from users.

By contributing to coMedia, this is what you get. A repository of your media interests, and a powerful media search engine for you to query.

## How does it work
There are three main functionalities. Searching for content, adding commentaries, and listing commentaries. These are accessible through a simple command line interface. To start, run:

`python main.py`

Enter a user Id. This should be a distinct name, to keep your contributions together. Next, enter which action you wish to perform. One of 'add', 'search and 'review'.

![Screenshot from 2024-09-22 22-38-32](https://github.com/user-attachments/assets/1d90cb1c-5492-49d1-a355-c219b524af21)

## Adding content

Whenever a user wants to add a commentary on a piece of content, it must provide with the following:
* (Optional) A set of bibliographic details: Author, date, location, language
* A description of the digital content, as objective as possible
* A comment on the content, including, at least, the best and worst parts of it according to the user. Never include personal or identifiable information.

After adding the commentary, the coMedia system will locate the most likely content entries already in the system, trying to match the new comment to existing content. This matching is done through a LLM embedding similarity of the available descriptions. Upon reviewing the most likely options, the users confirms one of the options, or rejects them all. If its confirmed, the commentary becomes associated with the existing content. If all are rejected, a new content is created using the bibliographic information and decription provided by the user.

## Searching content

The search for content considers the comments provided by users. These are embedded by an LLM, and matches against the search query. The most similar contents are retrieved for the user to review. Contents are represented by an aggregation and summarization of all comments available for it. 

## Listing content

Simply, get all the comments added by the active user.

## Embedding actions

As a working prototype, considering the many changes happening in the persisted data, an external procedure is provided, so that one can produce the LLM embeddings for all data. This is computed through the embed_main.py call, which processes the xml file and generates the embeddings and stores them in a pkl.

In other words, you need to run 'python embed_main.py' after adding some comments to the system, so these are embedded by the LLM model and accessible through the search functionality.

## Disclaimer
This is the prototype of a prototype. Important pieces are missing, such as proper user management, interface and privacy. 

