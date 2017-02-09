total_bill = float(raw_input("Total bill amount? "))
service = raw_input("Level of service? ")
good = float(0.20 * total_bill)
fair = float(0.15 * total_bill)
bad = float(0.10 * total_bill)
good_bill = float(good + total_bill)
fair_bill = float(fair + total_bill)
bad_bill = float(bad + total_bill)
if service == "good":
    print "Tip amount: %0.2f" % good
    print "Total amount: %0.2f" % good_bill
elif service == "fair":
    print "Tip amount: %0.2f" % fair
    print "Total amount: %0.2f" % fair_bill
elif service == "bad":
    print "Tip amount: %0.2f" % bad
    print "Total amount: %0.2f" % bad_bill
