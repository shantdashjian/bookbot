def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def sort_char_dictionary(dict):
    keys = list(dict.keys())
    keys.sort(key=lambda item: dict[item], reverse=True)
    sorted_dict = {}
    for key in keys:
        sorted_dict[key] = dict[key]
    return sorted_dict

def print_report(filepath, num_words, char_dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    char_dictionary_sorted = sort_char_dictionary(char_dictionary)
    for key in char_dictionary_sorted.keys():
        if key.isalpha():
            print(f"{key}: {char_dictionary_sorted[key]}")
    
    print("============= END ===============")