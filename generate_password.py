
#       ###  FIRST SOLUTİON  ###

import random

def password():
  while True:
     name = input("Enter your name: ") 
     random_number = str(random.randint(1000,9999))
     if name.lower() == "exit" :
         print("Exiting the program... Good Bye")
         break
     password_1 = ""
     for i in range(3):
         part_1 = random.choice(name)
         password_1 = password_1 + part_1.lower()   
     print(password_1+random_number)
  return 
password()


        ###  SECOND SOLUTİON  ###

import random as rnd

name = input("Please enter your full name (without any space): ")
passw = ""
for i in range(3):
  randIndex = rnd.randint(0, len(name)-1)
  letter = name[randIndex]
  passw += letter.lower()
  
randNum = rnd.randint(1000,9999)
passw += str(randNum)
print(passw)




