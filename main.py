import sys
sys.path.append('src')

from src.content_manager import ContentManager
from src.content import Content

def main():
    content_manager = ContentManager("data/contents.xml")

    user_id = input("Enter user ID: ")

    while True:
        action = input("Enter action (add, search, review): ")
        if action == "add":
            author_id = user_id
            co_type = "commentary"
            description = input("Enter description: ")
            language = input("Enter language: ")
            author = input("Enter author name: ")
            place = input("Enter place: ")
            score = int(input("Enter score (1-5): "))
            link = input("Enter link: ")
            date_str = input("Enter date:")

            content = Content(
                author_id, co_type, description, language, author,
                date_str,
                place, score, link
            )
            content_manager.add_content(content)
            print("Content added successfully.")
        elif action == "search":
            query = input("Enter search query: ")
            results = content_manager.search(query)
            # ... display results
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
                print("No content found for the user.")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()