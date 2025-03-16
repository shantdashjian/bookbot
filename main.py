from stats import get_num_words, get_num_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary = get_num_characters(text)
    sorted_dictionary = sort_dictionary(dictionary)

    # Generate Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("# --------- Character Count -------")
    for entry in sorted_dictionary:
        key = entry["char"]
        value = entry["num"]
        print(f"{key}: {value}")
    print("============= END ===============")
main()