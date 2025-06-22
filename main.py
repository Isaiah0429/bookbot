def get_book_text(filepath_to_book):
    with open(filepath_to_book) as book:
        book_text = book.read()
    return book_text

def main():
    filepath_to_book = "books/frankenstein.txt"
    print(get_book_text(filepath_to_book))

main()