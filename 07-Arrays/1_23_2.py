import MyEx123

text_input = "An apple a day keeps the doctor away"

words_count = MyEx123.count_words(text_input)

words_by_length = MyEx123.sort_by_length(text_input)

words_alphabetically = MyEx123.sort_alphabetically(text_input)

print(f"Liczba słów w tekście: {words_count}")
print(f"Słowa posortowane według długości: {words_by_length}")
print(f"Słowa posortowane alfabetycznie: {words_alphabetically}")

