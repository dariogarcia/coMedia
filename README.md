# coMedia
This platform is designed to store (1) digital content and (2) your comments about it. It is intended to provide you with a personal repository of content you care for. A place where you can store all that you read, watch and listen, and want to remember. Wanna enjoy it again in the future? Store it in coMedia. Once populated, using its natural language AI tech, coMedia can repond to your detailed requests. A second brain for digital content, with a search engine powered by a universal and collaborative database of quality consumer media. Data privacy provided through anonimization, aggregation and embeddings.

The coMedia platform is composed of a user and a server side. Users index favourite content, and add comments to it, which never leave the user side in textual form. Servers host a global list of contents, by matching and merging the ones created by users. User comments, anonimized, aggregated and embedded, are used to characterize content on the server side. 

## User Functionalities
The main functionalities, detalied below, are the ones available from the user side of the platform:
* Add new content to your personal list of favourite media
* Add comments to your content, for indexing and later retrieval
* Search for content within your favourites
* Make queries to the server side for new content 

### Add new user content

For a user to add new elements to its own list of liked content, it must provide bibliographic details that allow to identify it, such as author, date, location, language or url, and store it. These details are sent to the server, which return a list of possible matches, for the user to accept or reject. Upon acceptance, the entry from the user list becomes linked and enriched. Together with the bibliographic details, the user can provide a description of the digital content, as objective as possible, in natural language and short (e.g., 3 to 10 sentences). Finally, the user can also provide a comment on the content, including what makes it more enjousable, in which context it is best consumed.

The information described above is the one used to respond to queries from the user. Thus, a user who introduces information of high quality will be able to access its own data most successfully. Users will be prompt on that, together with the rule of never including personal or identifiable information in any field.

After adding the commentary, the coMedia system will locate the most likely content entries already in the system, trying to match the new comment to existing content. This matching is done through a LLM embedding similarity of the available descriptions. Upon reviewing the most likely options, the users confirms one of the options, or rejects them all. If its confirmed, the commentary becomes associated with the existing content. If all are rejected, a new content is created using the bibliographic information and decription provided by the user.


### Add new user comment

### Search for old user content

### Search for new user content

## Server Functionalities

The main services running on the server side of the platform are:
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

## Listing content
Simply, get all the comments added by the active user.

## Embedding actions

As a working prototype, considering the many changes happening in the persisted data, an external procedure is provided, so that one can produce the LLM embeddings for all data. This is computed through the embed_main.py call, which processes the xml file and generates the embeddings and stores them in a pkl.

In other words, you need to run 'python embed_main.py' after adding some comments to the system, so these are embedded by the LLM model and accessible through the search functionality.

# Disclaimer
This is the prototype of a prototype. Important pieces are missing, such as proper user management, interface and privacy (e.g., data anonymization). Dont ever submit personal information, misinformation, or any other sort of illegal content.

