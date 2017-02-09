product = 0
for x in range(11):
  for y in range(11):
      product = int(x * y)
      if x * y > 0:
        print "%r * %r = %r" % (x, y, product)
