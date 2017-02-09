height = int(raw_input("What is the height? "))
width = int(raw_input("What is the width? "))
border = '*' * width

if height == 1:
    if width == 1:
        print '*'
    else:
        print border
elif width == 1:
    for x in range(int(height)):
        print '*'
elif height == 2:
    for x in range(int(height)):
        print border
elif height > 2:
    print border
    for x in range(int(height)):
        print "*" + (" " * int((int(width) - 2))) + "*"
    print border
