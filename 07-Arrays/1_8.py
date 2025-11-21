#Write a program that prints a popular computer games, each game 
# name on a separate line. Use the while statement. Additionally, number the
#  list (print the next number before each list item) and sort the list
#  alphabetically (use one of a Python built-in functions for sorting)

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sort the list alphabetically
computer_games.sort()

# Initialize counter
i = 0

# Use while loop to print each game with numbering
while i < len(computer_games):
    print(f"{i + 1}. {computer_games[i]}")
    i += 1


