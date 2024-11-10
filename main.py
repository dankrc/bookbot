def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counted_words = word_count(text)
    num_chars = dict_to_list(char_count(text))
    num_chars.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---") 
    print(f"{counted_words} words found in the document")
    for char in num_chars:
        if char["name"].isalpha():
            print(f"The '{char['name']}' character was found {char['num']} times")
    print("--- End report ---")

def dict_to_list(dict):
    list_of_dict = []
    for d in dict:
        item = {"name": d, "num": dict[d]}
        list_of_dict.append(item)
    return list_of_dict

def sort_on(dict):
    return dict["num"]

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowered_text = text.lower()
    chars = set(lowered_text)
    num_chars = {}
    for char in chars:
        num_chars[char] = 0
    for char in lowered_text:
        num_chars[char] += 1
    return num_chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
