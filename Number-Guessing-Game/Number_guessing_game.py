import random

x=str(input("Choose difficulty. 'easy', 'medium', 'hard':")).lower()

if x == "easy":
  n=random.randint(1,50)
  y=20
elif x == "medium":
  n=random.randint(1,100)
  y=12
elif x == "hard":
  n=random.randint(1,200)
  y=10

attempts=1
max_attempts=y-1
comp_choice=n
user_choice=int(input("Enter your guess:"))
while True:
   if user_choice > comp_choice :
      print("Wrong guess. Too high.")
      print("attempts remaining= ",max_attempts)
   elif user_choice < comp_choice :
      print("Wrong guess. Too low.")
      print("attempts remaining= ",max_attempts)
   else:
      print("Congratulation, You won.")
      print("You took ",attempts," attempts to guess it.")
      break
      
   user_choice=int(input("Enter your guess:"))
   attempts += 1
   max_attempts -= 1
   if max_attempts == 0:
     print("Game Over Buddy................")
     break