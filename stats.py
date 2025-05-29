def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dictionary(text):
    dict = {}
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_char_dictionary(dict):
    keys = list(dict.keys())
    keys.sort(key=lambda item: dict[item], reverse=True)
    sorted_dict = {}
    for key in keys:
        sorted_dict[key] = dict[key]
    return sorted_dict