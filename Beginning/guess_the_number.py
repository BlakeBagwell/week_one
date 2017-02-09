import random
my_random_number = random.randint(1, 10)
guessCount = 1
guess = int(raw_input("Guess a number between 1 and 10!"))
while guessCount < 5:
    if guessCount == 5:
        print "Out of tries!"
        if raw_input("Play again?") == "yes":
            guessCount = 1
            my_random_number = random.randint(1,10)
        else:
            "Bye!"
            break
    elif guess != my_random_number:
        if guess < my_random_number:
            guess = int(raw_input("Too low, guess again!"))
            guessCount = guessCount + 1
        else:
            guess = int(raw_input("Too high, guess again!"))
            guessCount = guessCount + 1
        if guess == my_random_number:
                print "You win!"
                if raw_input("Play again?") == "yes":
                    guessCount = 1
                    my_random_number = random.randint(1,10)
                else:
                    "Bye!"
