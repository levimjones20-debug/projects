import random
secret = random.randint(1, 100)
guesses = 0
print("guess a number between 1 and 100!")
while True:
    guess = int(input("your guess: "))
    guesses = guesses + 1
    if guess < secret: 
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("spot on!")
        print(f"you got it in {guesses} guesses!")
        break
    
