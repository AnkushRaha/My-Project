import random 
import time

choices= ["STONE", "PAPER", "SCISSOR"]
print("\t\t\t\t\t\t WELCOME PLAYER.......")
print("---------------- ' STONE, PAPER, SCISSOR GAME  :) ' ---------------- ")
user_score=0
comp_score=0
while True:
  user_choice=input("Enter Your Choice (STONE, PAPER, SCISSOR) Or Enter Exit To Exit:").upper()
  if user_choice == "EXIT":
    print("Creating The Final Result.....")
    print("Loading..........")
    time.sleep(1)
    print(f"Final Score--- You {user_score} And Computer {comp_score}")
    if user_score > comp_score:
      print("You Are The Champion..... :D")
    elif user_score == comp_score:
      print("It's A Tie MAtch.....")
    else:
      print("Better Luck Next Time.....")
    print("Bye...See You Later........")
    break
  elif user_choice not in choices:
    print("Invalid Input........ :( ")
    continue
  print("waiting for computer to choose...")
  time.sleep(1)
  comp_choice= random.choice(choices)
  print("You Choose: ",user_choice)
  print("Computer Choose: ",comp_choice)

  if user_choice == comp_choice:
     print("Its A Tie.")
  elif (user_choice == "SCISSOR" and comp_choice == "PAPER") or\
   (user_choice == "STONE" and comp_choice == "SCISSOR") or\
   (user_choice == "PAPER" and comp_choice == "STONE"):
     print("You Win.")
     user_score += 1
  else:
     print("You Lose.")
     comp_score += 1
  
  print(f"Your Score {user_score}, Computer Score {comp_score}")