#main.py
import sys
from stats import get_word_count, get_character_count, sort_character_count_dictionary

def main():
    if len(sys.argv) != 2: # checks if the number of argument values provided to the system are equal to 2
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    character_count_sorted = sort_character_count_dictionary(character_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in character_count_sorted:
        if i["char"].isalpha(): # Checks if the "char" of the dictionary is an alpha-numerical character
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


def get_book_text(file_path): # returns the contents of the file opened by using f.read()
    with open(file_path) as f:
        return f.read()

main()