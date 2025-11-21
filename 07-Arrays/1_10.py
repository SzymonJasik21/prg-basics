#The array contains the student's test results. A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer. Write a program that prints information about the test results:

#Number of questions:
#Number of correct answers:
#Number of incorrect answers:
#Percentage of correct answers:
###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# Prints test statistics
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if answer:   # True means correct
        correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers

# calculates the percentage of correct answers
percentage_correct = (correct_answers / question_number) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', f"{percentage_correct:.2f}%")