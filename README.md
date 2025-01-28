# coMedia
This platform is designed to store (1) digital content and (2) your comments about it. It is intended to provide you with a personal repository of content you care for. A place where you can store all that you read, watch and listen, and want to remember. Wanna enjoy it again in the future? Store it in coMedia. Once populated, using its natural language AI tech, coMedia can repond to your detailed requests. A second brain for digital content, with a search engine powered by LLMs. To enable a universal and collaborative database of quality consumer media, coMedia implements an asocial media, one without attention economy mechanisms. Data privacy is implemented through anonimization, aggregation and embeddings.

The coMedia platform is composed of a user and a server side. Users index favourite content, and add comments to it, which never leave the user side in textual form. Servers host a global list of contents, by matching and merging the ones created by users. User comments, anonimized, aggregated and embedded, are used to characterize content on the server side. 

## User Functionalities
The main functionalities, detalied below, are the ones available from the user side of the platform:
* Add new content to your personal list of favourite media
* Add comments to your content, for indexing and later retrieval
* Search for content within your favourites
* Make queries to the server side for new content 

### Add new user content and comments

For a user to add new elements to its own list of liked content, it must provide bibliographic details that allow to identify it, such as author, date, location, language or url, and store it. These details are sent to the server, which return a list of possible matches, for the user to accept or reject. Upon acceptance, the entry from the user list becomes linked and enriched. 

Together with the bibliographic details, the user can provide a description of the digital content, as objective as possible, in natural language and short (e.g., 3 to 10 sentences). Finally, the user can also provide a comment on the content, including what makes it more enjoiable, in which context it is best consumed, what it compares to, etc.

The information described above is the one used to respond to future queries from the user. Thus, a user who introduces information of high quality will be able to access its own data most successfully. Users will be prompt with details and tips on that, together with the rule of never including personal or identifiable information in any field.

The new user content is matched with the server repository using all three fields. The description and the commentary are passed anonymized and encoded as textual embeddings for semantic simlarity. Bilbiographic details are directly matched.

### Search for old/new user content

Users can query the plarform, looking for content entries. This can be done on the own listing of entries, to retrieve details of old content stored before, or it can be done on the server side which includes all content entries created by other users. Queries must follow the writing guidelines used for adding content. That is, include a brief description of what you are looking for, in which language, how you would like it to be, what you want it for, etc. User decides which set of features to use (bibliographic, descriptions, comments).

## Server Functionalities

The main services running on the server side of the platform are:
* Keep an integrated and updated list of all content
* Build an aggregated comment-based characterization of content
* Answer search queries from users

### Content Repository

In order to allow the collaborative construction of a knowledge base, the server integrates all content added by users. It maintains a database of unique contents, associated with multiple user entries (i.e., several users refering to the same content). This is mainly done through bilbiographic matching (author name, urls (wikipedia, imdb, spotify, youtube, podcast platforms, etc.) ) and remains pending until validated by user. Description and commentary of users anynimized and encoded, is stored associated with the content id, for retrieval purposes.

### Retrieval of the knowledge base

Users can make queries for content. Depending on user selection, this search is done using the different metadata types. 

# Data Structures

## Content
This structure is the atomic unit of media. Users keep a list with their own version of data, and the server keeps an aggregated view with frequencies, together with an embedded version of the content (also with frequencies for efficient storage). Content on the user side includes a unique identified, a list of bibliographic features, and a textual description.

User Content: uid, modality, author, title, date, location, language, url, imdb_link, wiki_link, yt_link, spot_link, goodreads_link, ..., description.

Server Content: uid, [<modality,freq>], [<title,freq>], ..., [<embedded_description,freq>].

## Commentary
Commentaries are the subjective view on content. Each comment is associated to a unique content. Frequency for avoid storing similar embeddings.

User Commentary: content_uid, commentary

Server Comentary: content_uid, [<embedded_commentary,freq>]

# Deprecated Prototype

Some test functionalities are under testing. These are accessible through a simple command line interface. To start, run:

`python main.py`

Enter a user Id. This should be a distinct name, to keep your contributions together. Next, enter which action you wish to perform. One of 'add', 'search and 'review'. This is an example of search:

![Screenshot from 2024-09-22 22-38-32](https://github.com/user-attachments/assets/1d90cb1c-5492-49d1-a355-c219b524af21)

## Embedding actions

As a working prototype, considering the many changes happening in the persisted data, an external procedure is provided, so that one can produce the LLM embeddings for all data. This is computed through the embed_main.py call, which processes the xml file and generates the embeddings and stores them in a pkl.

In other words, you need to run 'python embed_main.py' after adding some comments to the system, so these are embedded by the LLM model and accessible through the search functionality.

## Disclaimer
This is the prototype of a prototype. Important pieces are missing, such as proper user management, interface and privacy (e.g., data anonymization). Dont ever submit personal information, misinformation, or any other sort of illegal content.

