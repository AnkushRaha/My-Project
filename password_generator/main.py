import gen 

while True:
   print(": WELCOME TO PASSWORD GENERETER :")
   print("-----------------------------------------------------------")
   lenn = int(input("Enter The Length Of Your Password:"))
   use_upper= input("Do You Want Upper-Chase: (Enter Y to confirm):").upper()
   use_lower= input("Do You Want Lower-Chase: (Enter Y to confirm):").upper()
   use_sym= input("Do You Want Symbol: (Enter Y to confirm):").upper()
   use_num= input("Do You Want Number: (Enter Y to confirm):").upper()
   print("Your Password is:-------------- ")
   
   xx = gen.main_gen(lenn,use_upper,use_lower,use_num,use_sym)
   print(xx)