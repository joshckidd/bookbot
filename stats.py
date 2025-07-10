def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    char_counts = {}
    for char in book_text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_character_counts(char_counts):
    sorted_counts = []
    for key in char_counts:
        sorted_counts.append({"char": key, "num": char_counts[key]})
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
    
