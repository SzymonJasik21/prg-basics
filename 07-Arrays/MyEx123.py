def count_words(text):
    words = text.split()
    return len(words)
def sort_by_length(text):
    words = text.split()
    words.sort(key=len, reverse = True)
    return words
def sort_alphabetically(text):
    words = text.split()
    words.sort(key=str.lower)
    return words


