
coin = raw_input('Do you want a coin?')
coinTotal = 0
while coin == 'yes':
    coinTotal = coinTotal + 1
    print 'You have %d coins!' % coinTotal
    coin = raw_input('Do you want a coin?')
if coin == "no":
    print "Bye"

#Another solution
#num_coins = 0
#print "You have %d coins." % num_coins
#switch = raw_input("Do you want another? (yes/no)")
#while switch == "yes":
#    num_coins += 1
#    print "You have %d coins." % num_coins
#    switch = raw_input("Do you want another? (yes/no)")
# you don't need an if statement (technically) here
#print "Bye!"
