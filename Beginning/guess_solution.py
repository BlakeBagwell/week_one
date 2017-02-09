import random
play_again = "yes"
while play_again == "yes":
    guess_tried = 0
    secret_number = random.randint(1, 10)
    print "Guess between 1 and 10."
    while True:
        while True:
            guess_left = 5 - guess_tried
            print "You have %d guesses left" % guess_left
            if guess_tried == 5:
                print "No more guesses!"
                break

            guess = int(raw_input("Number?"))
            guess_tried += 1
            if guess == secret_number:
                print "You win!"
                break

            elif guess > secret_number:
                print "Too high!"

            elif guess < secret_number:
                print "Too low!"

            else:
                print "Nope, try again!"
    play_again = raw_input("Do you want to play again? (yes/no)")
    if play_again == "no":
        print "Bye!"
        break


### not working
