print("\n\n")
print("Hello, We'll play a small game with")
print("You will guess a number from 1 to 100")
print("if you guessed the true number you'll win")
print("be carefull that you have just 5 attempts.")

from random import randint
number = randint(1, 100)
print(number)

i = 0
while i < 5:
    x = int(input(f"{i+1}.attempt, guess a number: "))
    if x == number:
        print("congratulations, You win")
        break
    i += 1
    
if i == 5:
    print("Game over!")