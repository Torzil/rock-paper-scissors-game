from random import randint

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
computer_random_number = randint(1,3)
computer_move = ""
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
outcome = ""

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Please try again!")

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

if (player_move == rock and computer_move == scissors) or \
(player_move == paper and computer_move == rock) or \
(player_move == scissors and computer_move == paper):
    outcome = "You win!"
elif player_move == computer_move:
    outcome = "Draw!"
else:
    outcome = "You lose!"

print(f"You chose {player_move}.")
print(f"The computer chose {computer_move}.")
print()
print(outcome)
