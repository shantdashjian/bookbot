from stats import get_num_words, get_num_characters, sort_dictionary
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
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