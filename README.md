# coMedia

This project persists and provides an index for media (text, sound, video, interactive or otherwise), as reviewed by users. For retrieval and merging it uses LLM embeddings.

There are currently three main functionalities considered. Adding commentaries, searching for content, and listing commentaries.

## Adding content

Whenever a user wants to add a commentary on a piece of content, it must provide with the following:
* (Optional) A set of bibliographic details: Author, date, location, language
* A description of the digital content, as objective as possible
* A personal comment on the content, including, at least, the best and worst parts of it according to the user

After adding the commentary, the coMedia system will locate the most likely content entries already in the system, trying to match the new comment to existing content. This matching is done through a LLM embedding similarity of the available descriptions. Upon reviewing the most likely options, the users confirms one of the options, or rejects them all. If its confirmed, the commentary becomes associated with the existing content. If all are rejected, a new content is created using the bibliographic information and decription provided by the user.

## Searching content

The search for content considers the comments provided by users. These are embedded by an LLM, and matches against the search query. The most similar contents are retrieved for the user to review. Contents are represented by an aggregation and summarization of all comments available for it. 

## Listing content

Simply, get all the comments added by the active user.

## Embedding actions

As a working prototype, considering the many changes happening in the persisted data, an external procedure is provided, so that one can produce the LLM embeddings for all data. This is computed through the embed_main.py call, which processes the xml file and generates the embeddings and stores them in a pkl.
