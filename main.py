from stats import get_num_words, get_char_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    text = get_book_text("./books/frankenstein.txt")

    num_words = get_num_words(text)
    char_dictionary = get_char_dictionary(text)

    print(f"{num_words} words found in the document")
    print(char_dictionary)

main()