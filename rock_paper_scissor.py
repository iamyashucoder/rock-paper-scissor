rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""") 
import random
print("Welcome to Rock, Paper, Scissors Game!")
computer_options = [rock, paper, scissor]
your_choice = input("What do you choose? Rock, Paper or Scissors.").lower()    
computer_choice = (random.choice(computer_options))
print(computer_choice)
if your_choice == "rock" :
    your_art = rock
elif your_choice == "paper" :
    your_art = paper
elif your_choice == "scissors" :
    your_art = scissor
else:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")
    exit()
print(your_art)

if your_art == computer_choice:
    print("It's a draw!")
elif (your_art == rock and computer_choice == scissor) or \
     (your_art == paper and computer_choice == rock) or \
     (your_art == scissor and computer_choice == paper):    
    print("You win!")
else:
    print("You lose!")  