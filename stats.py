def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in char_count:
            char_count[char_lower] = 1
        else:
            char_count[char_lower] += 1
    return char_count

def sort_on(char_num):
    return char_num["num"]

def get_sorted_list_of_char_count(char_count):
    sorted_char_count = []
    for key in char_count:
        sorted_char_count.append({"char": key, "num": char_count[key]})
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count
    