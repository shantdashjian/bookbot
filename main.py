def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def get_num_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()