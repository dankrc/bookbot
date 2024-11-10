def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    counted_words = word_count(text)
    print(counted_words)
    num_chars = char_count(text)
    print(num_chars)

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
