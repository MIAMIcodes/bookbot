def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in char_dict:
            char_dict[lower_c] += 1
        else:
            char_dict[lower_c] = 1
    return char_dict

def sort_dict(char_dict):
    in_order = dict(sorted(char_dict.items(), key=lambda x:x[1],reverse=True))
    return in_order
