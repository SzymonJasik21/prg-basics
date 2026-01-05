import random

computer = random.randint(1, 6)

you = int(input('Enter your guess (1-6): '))

win = computer == you

print(f'Computer rolled: {computer}')
print(f'You won: {win}')