import random
num = random.randint(1,100)
flag=None
while flag!=num:
    try:
        guess = int(input("Enter number: "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print("Congratulations! You guessed the number. ")
    except ValueError:
            print("Please enter a valid number.")
