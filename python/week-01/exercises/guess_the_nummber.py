__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

#Guess the number game

import random
secret = random.randint(1, 10)
count = 0

while True:
    tahmin = int(input("Guess the number between 1 and 10: (or type 0 to exit)"))
    if tahmin == 0:
        print("Game exited.")
        break
    
    count += 1
    
    if tahmin == secret:
        print("Congratulations! You guessed the number correctly.")
        print(f"{count} guesses to get it right")
        continue_game = input("Do you want to play again? (yes/no): ")
        if continue_game.lower() == "yes":
            secret = random.randint(1, 10)
            count = 0
            continue
        else:
            print("Thanks for playing!")
            break
    elif tahmin > secret:
        print("Please enter a smaller number")
    elif tahmin < secret:
        print("Please enter a larger number")