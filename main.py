from src.item_manager import ItemManager, get_next_item_id
from src.item import Item

def main():
    item_manager = ItemManager("data/items.xml")
    user_id = input("Enter user ID: ")

    while True:
        #Loader
        action = input("Enter action (add, search, review): ")
        #Add new content or comment
        if action == "add":
            author_id = user_id
            item_type = "commentary"
            item_id = get_next_item_id(item_manager)
            description = input("Enter description: ")
            commentary = input("Enter commentary: ")
            try:
                score = int(input("Enter your score for content quality (1-5): "))
            except ValueError:
                score = 0
            language = input("If applicable, enter language of content: ")
            author = input("If known, enter author of original content: ")
            place = input("If known and applicable, enter location of original content: ")
            link = input("If possible, enter an external link to the original content: ")
            date_str = input("If known and applicable, enter a creation date for the original content:")
            media_id = item_manager.associate_content(description)
            item = Item(author_id, item_type, description, commentary, language, author, date_str, place, score, link, item_id, media_id)
            item_manager.add_item(item)
            print("Comment added successfully.")
        #Search for content
        elif action == "search":
            query = input("Enter search query: ")
            results = item_manager.retrieve_by_similarity(query,match_cont_desc=True,match_comm_comm=False)
            print("\n Most similar contents:")
            for content_desc, (_,similarity) in results:
                print(f"Description: {content_desc} (Similarity: {similarity:.4f})")
        #See previously added contents/comments
        elif action == "review":
            user_items = item_manager.get_user_items(user_id)
            if user_items:
                print("Your items:")
                for item in user_items:
                    print(f"Description: {item.description}")
                    print(f"Author: {item.author}")
                    print(f"Date: {item.date}")
                    print(f"Link: {item.link}")
                    print("---")
            else:
                print("No items found for this user.")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()