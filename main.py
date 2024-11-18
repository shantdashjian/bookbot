def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words_count = count_words(file_contents)
        characters_count = count_characters(file_contents)
        list = convert_to_sorted_list(characters_count)
        print_report(words_count, list)

def count_words(text):
    return len(text.split())

def count_characters(text):
    map = {}
    for char in text:
        char_to_lower = char.lower()
        if char_to_lower in map:
            map[char_to_lower] += 1
        else:
            map[char_to_lower] = 1
    return map

def convert_to_sorted_list(dict):
    list = []
    for char in dict:
            if char.isalpha():
                list.append({"char": char, "count": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(item):
    return item["count"]

def print_report(words_count, list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print()
    for item in list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")

main()