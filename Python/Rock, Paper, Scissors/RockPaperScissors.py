import random 

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue 

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Suck! You're a cheater!")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("You Suck! You're a cheater!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Suck! You're a cheater!")
        user_wins += 1

    else:
        print("You are GARBAGE, TERRIBLE, TRASH, BAD, HORRIBLE, EVERY OTHER NEGATIVE ADJECTIVE.")
        computer_wins += 20000000000000
   

print("You lost", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("See ya. Don't Comeback!")