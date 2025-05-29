from stats import get_num_words, get_char_dictionary, sort_char_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)

    num_words = get_num_words(text)
    char_dictionary = get_char_dictionary(text)
    char_dictionary_sorted = sort_char_dictionary(char_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for key in char_dictionary_sorted.keys():
        if key.isalpha():
            print(f"{key}: {char_dictionary[key]}")
    
    print("============= END ===============")
    
main()