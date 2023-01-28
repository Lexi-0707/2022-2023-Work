import random

# 1/12/23

diceRolls = []
randomNumber = 0 
overall = 0 
counter = 1

numberDice = int(input("Please input the number of dice you want to roll "))

# generates numbers and adds them togther and puts them in list 
for i in range(numberDice):
    randomNumber = random.randint(1, 6)
    overall += randomNumber
    diceRolls.append(randomNumber)

# prints out numbers in list as well as what number roll it was 
for num in diceRolls:
    print("Roll number", counter)
    print(num)
    counter += 1

# prints out total 
print("The overall total is:")
print(overall)

