from src.content_manager import ContentManager, get_next_co_id
from src.content import Content

def main():
    content_manager = ContentManager("data/contents.xml")
    user_id = input("Enter user ID: ")

    while True:
        #Loader
        action = input("Enter action (add, search, review): ")
        #Add new content or comment
        if action == "add":
            author_id = user_id
            co_type = "commentary"
            description = input("Enter description: ")
            language = input("If applicable, enter language of content: ")
            author = input("If known, enter author of original content: ")
            place = input("If known and applicable, enter location of original content: ")
            score = int(input("Enter your score for content quality (1-5): "))
            link = input("Enter an external link to the original content: ")
            date_str = input("If known and applicable, enter a creation date for the original content:")
            co_id = get_next_co_id(content_manager)
            media_id = "TODO"
            content = Content(author_id, co_type, description, language, author, date_str, place, score, link, co_id, media_id)
            content_manager.add_content(content)
            print("Content added successfully.")
        #Search for content
        elif action == "search":
            query = input("Enter search query: ")
            results = content_manager.search(query)
            print("\n Most similar contents:")
            for content_desc, similarity in results:
                print(f"Description: {content_desc} (Similarity: {similarity:.4f})")
        #See previously added contents/comments
        elif action == "review":
            user_contents = content_manager.get_user_contents(user_id)
            if user_contents:
                print("Your contents:")
                for content in user_contents:
                    print(f"Description: {content.description}")
                    print(f"Author: {content.author}")
                    print(f"Date: {content.date}")
                    print(f"Link: {content.link}")
                    print("---")
            else:
                print("No content found for this user.")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()