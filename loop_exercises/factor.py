factor_num = int(raw_input("Number to be factored?"))
factors = []

for x in range(factor_num + 1):
    if x > 0:
        if factor_num % x == 0:
            factors.append(x)
print factors
