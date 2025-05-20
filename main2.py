from stats import get_num_words, count_letters, sort_letter_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    word_count = get_num_words(text)
    letter_counts = count_letters(text)
    sorted_letters = sort_letter_counts(letter_counts)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for entry in sorted_letters:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

main()
