def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    dictionary = {}
    for char in text:
        key = char.lower()
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary