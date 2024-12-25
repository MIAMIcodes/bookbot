def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    # print(count_characters(text))
    print("")
    char_dict = count_characters(text)
    sorted_list = dict_sort(char_dict)
    for index in range(len(sorted_list)):
        for key in sorted_list[index]:
            print(f"The '{sorted_list[index]['char']}' character was found {sorted_list[index]['num']} times")
            break
    print("--- End report ---")
def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_dict = {}
    lowered_text = text.lower()
    individual_char = list(lowered_text)
    for char in individual_char:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_sort(dict):
    dict_list = []
    char_dict = {}
    for k in dict:
        if k.isalpha() == True:
            char_dict["char"] = k
            char_dict["num"] = dict[k]
            dict_list.append(char_dict)
            char_dict = {}
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list

main()