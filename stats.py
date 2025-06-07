#stats.py
def get_word_count(book_text): # returns number of words in document by splitting and then reading the length of the list
    return f"{len(book_text.split())}" 

def get_character_count(book_text):
    book = {}
    for i in book_text.lower():
       if i in book:
           book[f"{i}"] += 1
       else :
           book[f"{i}"] = 1
    return book

def sort_character_count_dictionary(character_count):
    character_count_sorted = []
    for i in character_count:
        new_dict = {"char": i, "num": character_count[i]}
        character_count_sorted.append(new_dict)
    character_count_sorted.sort(reverse = True, key=sort_on_num)
    return character_count_sorted

def sort_on_num(dict):
    return dict["num"]

def sort_on_char(dict):
    return dict["char"]