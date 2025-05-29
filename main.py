import sys
from stats import get_num_words, get_char_dictionary
from io_utils import get_book_text, print_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    num_words = get_num_words(text)
    char_dictionary = get_char_dictionary(text)
    print_report(path_to_book, num_words, char_dictionary)
    
main()