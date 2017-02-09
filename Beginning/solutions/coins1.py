num_coins = 0
print "You have %d coins." % num_coins
while True:
    switch = raw_input("Do you want another? (yes/no) ")
    if switch == 'yes':
        num_coins += 1
        print "You have %d coins." % num_coins
    elif switch == 'no':
        print "Bye"
        break
    else:
        print "Try again"
