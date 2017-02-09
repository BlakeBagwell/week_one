banner = raw_input("Banner name?")
border_line = (len(banner) * '*') + ('*' * 4)
middle_line = '* ' + banner + ' *'

for x in range(3):
    if x == 1:
        print middle_line
    else:
        print border_line
