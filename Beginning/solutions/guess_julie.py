import random

def play_again():
   play_again = (raw_input("Do you want to play again (Y or N)? ")).upper()
   if play_again == "Y":
       guess_number()
   else:
       print "Bye!"

def guess_number():
   secret_number = random.randint(1, 10)
   print "I am thinking of a number between 1 and 10."
   print "You have 5 guesses left."
   count = 4

   while count >= 0:
       guess = int(raw_input("What's the number? "))

       if guess == secret_number:
           print "Yes! You win!"
           play_again()
           break

       elif count == 0:
           print "You ran out of guesses! The secret number was %d" % secret_number
           play_again()
           break

       elif guess > secret_number:
           print "%d is too high." % guess
           print "You have %d guesses left." % count

       else:
           print "%d is too low." % guess
           print "You have %d guesses left." % count

       count -= 1

guess_number()
