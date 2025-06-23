# Importing necessary libraries
from stats import word_split
from stats import individual_characters
from stats import individual_characters_sorted

def get_book_text(filepath_to_book):
    with open(filepath_to_book) as book:
        book_text = book.read()
    return book_text


def main():
    filepath_to_book = "books/frankenstein.txt"
    print(get_book_text(filepath_to_book))
    print(f"{len(word_split(get_book_text(filepath_to_book)))} words found in the document")
    print(individual_characters(get_book_text(filepath_to_book)))
    print(individual_characters_sorted(individual_characters(get_book_text(filepath_to_book))))
main()