# coMedia
This platform is designed to store (1) digital content and (2) your comments about it. It is intended to provide you with a personal repository of appreciated content. A place where you can store all that you read, watch and listen, and want to remember. Wanna enjoy it again in the future? Store it in coMedia. Based on natural language AI tech, coMedia can repond to your detailed requests. A second brain for digital content, with a search engine powered by a universal and collaborative database of quality consumer media. Data privacy provided through anonimization, aggregation and embeddings.

coMedia has a user and a server side. User stores favourite content, and comments on it, which never leave the user side in textual form. Servers host a global list of contents, by matching and merging the ones created by users. User comments, anonimized, aggregated and embedded, are used to characterize content on the server side. 

## User Functionalities
The main functionalities for the user side of the platform are:
* Add new content to your personal list of favourite media
* Add comments to your content, for indexing and later retrieval
* Search for content within your favourites
* Make queries to the server side for new content 

## Server Functionalities

The main functionalities for the user side of the platform are:
* Keep an integrated and updated list of all content
* Build an aggregated comment-based characterization of content
* Answer search queries from users

# Current Prototype

Some test functionalities are under testing. These are accessible through a simple command line interface. To start, run:

`python main.py`

Enter a user Id. This should be a distinct name, to keep your contributions together. Next, enter which action you wish to perform. One of 'add', 'search and 'review'. This is an example of search:

![Screenshot from 2024-09-22 22-38-32](https://github.com/user-attachments/assets/1d90cb1c-5492-49d1-a355-c219b524af21)

## Searching content
The search engine considers both the descriptions and the comments provided by users. These are embedded by an LLM, and matched against the search query. The most similar contents are retrieved, and shown as results to the user.

To build effective queries, follow the same guidelines expressed for adding content. That is, include a brief description of what you are looking for, in which language, how you would like it to be, what you want it for, etc.

## Adding content
Whenever a user wants to store its own content, it must provide with the following:
* (Optional) A set of bibliographic details for matching: Author, date, location, language.
* A description of the digital content, as objective as possible. Between 3 and 10 sentences.
* +/-: A comment on the content, including, at for example, the best and worst parts of it, or in which context you think is best for consumption. Never include here personal or identifiable information.

After adding the commentary, the coMedia system will locate the most likely content entries already in the system, trying to match the new comment to existing content. This matching is done through a LLM embedding similarity of the available descriptions. Upon reviewing the most likely options, the users confirms one of the options, or rejects them all. If its confirmed, the commentary becomes associated with the existing content. If all are rejected, a new content is created using the bibliographic information and decription provided by the user.

## Listing content
Simply, get all the comments added by the active user.

## Embedding actions

As a working prototype, considering the many changes happening in the persisted data, an external procedure is provided, so that one can produce the LLM embeddings for all data. This is computed through the embed_main.py call, which processes the xml file and generates the embeddings and stores them in a pkl.

In other words, you need to run 'python embed_main.py' after adding some comments to the system, so these are embedded by the LLM model and accessible through the search functionality.

# Disclaimer
This is the prototype of a prototype. Important pieces are missing, such as proper user management, interface and privacy (e.g., data anonymization). Dont ever submit personal information, misinformation, or any other sort of illegal content.

