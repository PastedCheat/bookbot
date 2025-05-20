# stats.py

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def sort_letter_counts(letter_counts):
    sorted_items = sorted(
        letter_counts.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_items
