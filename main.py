from stats import get_num_words, get_char_dictionary
from io_utils import get_book_text, print_report

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_dictionary = get_char_dictionary(text)
    print_report(filepath, num_words, char_dictionary)
    
main()