import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
answer = random.randint(1, level)
while True:
    while True:
        try:
            guess = int(input("Guess: "))
            break
        except ValueError:
            pass
    if guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()