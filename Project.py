"""Choice Number"""

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big.Take a smaller guess..")


print("----GAME OVER----") 

"""Random Password Generator"""

import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print(random.choice("hello"))

val = random.choice([1, 2, 3])
val = random.choice(["a", "b", "c", "d", "e", "f"])
print(val)
pass_len = 8

charValues = string.ascii_letters + string.digits + string.punctuation


#list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])
print(res)

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Your random password is:", password) 