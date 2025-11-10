import sys
from stats import get_num_words, get_char_count, get_sorted_list_of_char_count

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_count = get_sorted_list_of_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_num in sorted_char_count:
        char = char_num["char"]
        num = char_num["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()