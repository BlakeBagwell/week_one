bill = float(raw_input("Bill?"))
service = raw_input("Level of service? (good, fair bad)")
tipPercent = 0

if service == "good":
    tipPercent = .2
elif service == "fair":
    tipPercent = .15
elif service == "bad":
    tipPercent = .1

tip = float(tipPercent * bill)
total = float(tip + bill)


print "$ %r for %s service. $ %r total." % (tip, service, total)

people = float(raw_input("Number of people?"))
split = total / people

print "%r per person." % split
