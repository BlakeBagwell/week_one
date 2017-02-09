import random
guess_counter = 1
random_number = random.randint(1, 10)
guess = int(raw_input("Guess a number between 1 and 10"))
play_again = "yes"
while guess_counter < 5:
    if guess == random_number:
        print "you win!"
        play_again = raw_input("Play again? (yes/no)")
        if play_again == "yes":
            random_number = random.randint(1, 10)
            guess_counter = 1
            guess = int(raw_input("Guess a number between 1 and 10"))
        else:
            print "Bye!"
            break
    elif guess < random_number:
        print "Too low!"
        guess_counter += 1
        guess = int(raw_input("Guess again!"))
    elif guess > random_number:
        print "Too high!"
        guess_counter += 1
        guess = int(raw_input("Guess again!"))
    elif guess_counter == 5:
        play_again = raw_input("Play again? (yes/no)")
        if play_again == "yes":
            random_number = random.randint(1, 10)
            guess_counter = 1
            guess = int(raw_input("Guess a number between 1 and 10"))
        else:
            print "Bye!"
            break
