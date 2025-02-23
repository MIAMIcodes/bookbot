from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_chars(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("------------ Character Count -----------")
    in_order_dict = sort_dict(char_count)
    for i in in_order_dict:
        if i[0].isalpha():
            print(f"{i}: {in_order_dict[i]}")
    print("============ END ============")

main()
