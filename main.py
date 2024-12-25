def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    print(count_characters(text))

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    chars = {}
    lowered_text = text.lower()
    individual_char = list(lowered_text)
    for char in individual_char:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()