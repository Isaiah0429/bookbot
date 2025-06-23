#Function to count the number of words in a book
def word_split(book_text):
    individual_words = book_text.split()
    return individual_words

#Function to count the invidividual characters in a book
def individual_characters(book_text):
    modified_book_text = book_text.lower()
    individual_characters_dict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
        "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
        "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
        "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
        "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
        "z": 0, " ": 0, "\n": 0, ".": 0, ",": 0,
        "!": 0, "?": 0, "'": 0, '"': 0, ";": 0,
        ":": 0, "-": 0, "(": 0, ")": 0, "[": 0,
        "]": 0,
    }
    for character in modified_book_text:
        if character in individual_characters_dict:
            individual_characters_dict[character] += 1
    return individual_characters_dict
# Sort function for individual characters
def individual_characters_sorted(individual_characters_dict):
    for character in individual_characters_dict:
         sorted_characters = individual_characters_dict[character].sort(reverse=True, key=sort_on)
    return sorted_characters