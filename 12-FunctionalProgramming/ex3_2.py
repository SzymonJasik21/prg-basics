sentence = "I completely agree with you"
result = list(map(lambda word : len(word) , sentence.split()))
print(f"Number of letter in sentence: {result}")