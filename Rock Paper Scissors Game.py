import random

computer = {"a": "rock", "b": "paper", "c": "scissors"}
group = ["rock", "paper", "scissors"]
while True:
    computer_choice = group[random.randint(0, 2)]
    player_choice = input('Type "rock", "paper" or "scissors": ')
    if player_choice not in group:
        player_choice = input("Incorrect input! Please retype: ")
    print("The computer's answer is:", computer_choice)
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "paper" or \
            player_choice == "paper" and computer_choice == "scissors" or \
            player_choice == "scissors" and computer_choice == "rock":
        print("You lose!! ")
    else:
        print("You win!! ")
    again = input('Try again? (Type "Y" or "N") ')
    if again == "Y":
        print()
        continue
    else:
        break

