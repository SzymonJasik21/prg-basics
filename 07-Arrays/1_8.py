
#computer_games = [
   #"Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
  # "League of Legends", "Valorant", "Grand Theft Auto V", 
 #  "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
#]

# Sort the list alphabetically
#computer_games.sort()

# Initialize counter
#i = 0

# Use while loop to print each game with numbering
#while i < len(computer_games):
 #   print(f"{i + 1}. {computer_games[i]}")
  #  i += 1

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()
#print(computer_games)

#start = 1

for index, game in enumerate(computer_games, 1):
      print(f"{index}. {game}")

#list_range = len(computer_games)

#for index in range (len(computer_games)):
 #     print(f"{index + 1}. {computer_games[index]}")


