height = int(raw_input("What is the height? "))
width = int(raw_input("What is the width? "))
if height < 3 and width < 3:
    if height == 1 and width == 1:
        print "*"
        break
    if height == 2 and width == 2:
        for x in range(2):
            print "**"
            break
#while True:
#    print "*" * width
#    for x in range(int(height)):
#
#        if x > 0 and x < int(width):
#            print "*" + (" " * (int(width) - 2)) + "*"
#    print "*" * width
