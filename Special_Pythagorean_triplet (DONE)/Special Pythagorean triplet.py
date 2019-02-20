

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 200
b = 1
c = 1
square = 0
added = 0
multiple = 0
multiSquare = 0
loops = 0

while a <= 200:
    # print ((a * a), a)
    while b <= 1000:
        while c <= 1000:
            loops = loops + 1
            added = a + b + c
            # square = (a * a) + (b * b) + (c * c)
            # multiSquare = (a * a) * (b * b) * (c * c)
            if ((a * a) + (b * b) == (c * c)):
                if (added >= 800) & (added <= 1000):
            # if (multiSquare >= 950) & (multiSquare <= 1050):
                    print ("added", added, a, b, c)
                    print (a * b * c)
            c = c + 1
        b = b + 1
        c = 1
    a = a + 1
    b = 1
print (loops)
print ((1 * 1) + (10 * 10) + (30 * 30))
