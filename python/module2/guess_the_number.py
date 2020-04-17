import random

number = random.randint(1, 100)
while True:
    print("I made up a number. Can you guess it?")

    try:
        user_guess = int(input())
    except ValueError:
        print("I said a NUMBER")
        continue
    if user_guess < number:
        print('Too low')
        continue
    elif user_guess > number:
        print('Too high')
        continue
    else:
        print("Congratulations you won!")
        break
