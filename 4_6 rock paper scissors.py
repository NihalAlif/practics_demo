rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock, paper, scissors]

# Get user's choice
while True:
    chose = int(input("What do you choose? Type 0 for Rock,1 for Paper, or 2 for Scissors or 'exit' to quit the game:"))
    if str(chose).lower() == 'exit':
        print("Exiting the game. Thanks for playing!")
        break
    elif chose >= 3 or chose < 0:
        print("You typed an invalid number")
    else:
        print(game_img[chose])

        # Generate computer's choice
        import random
        computer_chose = random.randint(0, 2)
        print(game_img[computer_chose])

        # Determine the winner
        if chose == 0:
            if computer_chose == 2:
                print("You win! Rock crushes Scissors.")
            elif computer_chose == 1:
                print("You lose! Paper covers Rock.")
            else:
                print("It's a draw!")
        elif chose == 1:
            if computer_chose == 0:
                print("You win! Paper covers Rock.")
            elif computer_chose == 2:
                print("You lose! Scissors cut Paper.")
            else:
                print("It's a draw!")
        elif chose == 2:
            if computer_chose == 1:
                print("You win! Scissors cut Paper.")
            elif computer_chose == 0:
                print("You lose! Rock crushes Scissors.")
            else:
                print("It's a draw!")
        else:
            print("Invalid choice. Please choose 0, 1, or 2.")
