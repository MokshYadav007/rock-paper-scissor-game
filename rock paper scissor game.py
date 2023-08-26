import random
lst = ['r', 'p', 's']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
 
print(" \t \t \t \t Rock,Paper,Scissor Game \n\n")
print("r for rock\np for paper\ns for scissor")

while no_of_chance < chance:
    _input = input('Rock,Paper,Scissor:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie zero point to each\n")

    elif _input == "r" and _random == "p":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "r" and _random == "s":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("human wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "p" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "p" and _random == "r":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("human wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "s" and _random == "r":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "s" and _random == "p":
        human_point = human_point + 1
        print(f"Your guess {_input} and computer guess is {_random}\n ")
        print("human wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    else:
        print("you have input wrong\n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n ")

print("Game Over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you lose")

else:
    print("You win and computer lose")

print(f"your point is {human_point} and computer point is {computer_point}")
