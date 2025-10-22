import random
import config

def charpool(use_upper,use_lower,use_num,use_sym):
  char_pool= ""
  if use_upper == "Y":
    char_pool = char_pool + config.let_up
  if use_lower == "Y" :
    char_pool = char_pool + config.let_dw
  if use_num == "Y" :
    char_pool = char_pool + config.nums
  if use_sym == "Y" :
    char_pool = char_pool + config.sp_sym
  return char_pool

def val_check(lenn):
  if lenn > 0 and lenn < 256 :
    return True
  else:
    print("Enter A Valid Number Greater Than 0 And Less Than 256")
    return False

def pass_gen(lenn, char_pool):
    if not char_pool:
        print("Error: No character set selected! Choose at least one type.")
        return None
    password = ""
    while len(password) < lenn:
        password += random.choice(char_pool)
    return password

def main_gen(lenn,use_upper,use_lower,use_num,use_sym):
   if val_check(lenn):
     pool = charpool(use_upper,use_lower,use_num,use_sym) 
     password = pass_gen(lenn, pool)
     return password
   else:
     print("Password not generated due to invalid length.")
   return password