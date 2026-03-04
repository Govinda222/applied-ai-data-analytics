import random

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
c_moves = [rock,paper,scissors]
move = ""
human_moves = input("Enter your move \n1.rock \n2.paper \n3.scissor : ")
if human_moves.lower() == "rock" or human_moves == "1":
    move = rock
elif human_moves.lower() == "paper" or human_moves == "2":
    move = paper
elif human_moves.lower() == "scissors" or human_moves == "3":
    move = scissors
else:
    print("enter a valid move")
auto_moves = random.choice(c_moves)
if auto_moves == rock and move == rock or auto_moves == paper and move == paper or auto_moves == scissors and move == scissors:
    print(f" human move is : \n{move}")
    print(f"computer move is : \n{auto_moves}")
    print("Its a tie")
elif auto_moves == paper and move == rock or auto_moves == rock and move == scissors or auto_moves == scissors and move == paper:
    print(f" human move is : \n{move}")
    print(f"computer move is : \n{auto_moves}")
    print("Computer wins")
elif auto_moves == scissors and move == rock or auto_moves == paper and move == scissors or auto_moves == rock and move == paper:
    print(f" human move is : \n{move}")
    print(f"computer move is : \n{auto_moves}")
    print("Human wins")
else :
    print("Invalid move by human")