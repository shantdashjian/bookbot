from stats import get_num_words, get_char_count

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f"Found {num_words} total words")
    print(char_count)

main()