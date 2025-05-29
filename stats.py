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