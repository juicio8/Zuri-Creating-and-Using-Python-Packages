import random   #importing python package
#naming variables
rock = "R"        
paper = "P"
scissors = "S"
print("ROCK, PAPER, SCISSORS")
print("....loading")
player1 = input("Enter your name: ")
player1 = player1.upper()


isrunning = True
while isrunning:
    print("Enter R for rock, P for paper, S for scissors")
    #asking for player's choice
    player_input = input("Enter Choice: ")
    player_choice = player_input.upper()
    if player_choice == rock:
        print("ACCEPTED")
    elif player_choice == paper:
        print("ACCEPTED")
    elif player_choice == scissors:
        print("ACCEPTED")
    else:
        print("Enter valid choice")
        continue
    #CPU's choice
    #creating a list
    computer = [rock, paper, scissors]
    computer_choice = (random.choice(computer))
    print(f"{player1}({player_choice}) : CPU({computer_choice})")
    if computer_choice == rock and player_choice == scissors:
        print(f"{player1} LOST!")
    elif computer_choice == scissors and player_choice == rock:
        print(f"{player1} WINS!")
    elif computer_choice == rock and player_choice == paper:
        print(f"{player1} LOST!")
    elif computer_choice == paper and player_choice == rock:
        print(f"{player1} LOST!")
    elif computer_choice == scissors and player_choice == paper:
        print(f"{player1} LOST!")
    elif computer_choice == paper and player_choice == scissors:
        print(f"{player1} WINS!")
    else:
        print("IT'S A TIE!")
        continue
    isrunning = False
        
