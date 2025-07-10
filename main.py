from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_character_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_char_counts:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["num"]}")

main()

