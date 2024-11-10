def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    counted_words = word_count(text)
    print(counted_words)
def word_count(text):
    words = text.split()
    return len(words)




def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
