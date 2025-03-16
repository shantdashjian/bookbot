def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    dictionary = {}
    for char in text:
        key = char.lower()
        if key in [" ",  "\n"]:
            continue
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary

def sort_on(item):
    return item["num"]

def convert_to_list_of_dictionaries(dictionary):
    list_of_dictionaries = []
    for key in dictionary:
        list_of_dictionaries.append({
            "char": key,
            "num": dictionary[key]
        })
    return list_of_dictionaries

def sort_dictionary(dictionary):
    list_of_dictionaries = convert_to_list_of_dictionaries(dictionary)
    return sorted(list_of_dictionaries, key=sort_on, reverse=True)