# main.py
import sys
from stats import count_words, count_letters, sort_letter_counts

def print_report(book_path, word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    sorted_letters = sort_letter_counts(letter_count)
    for char, count in sorted_letters:
        print(f"{char}: {count}")

    print("--- End report ---")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    word_count = count_words(text)
    letter_count = count_letters(text)

    print_report(book_path, word_count, letter_count)

if __name__ == '__main__':
    main()
