from math import sqrt

def addPrime(current):
    definitePrime.append(current)

num = 5
target = 150000
current = 2
total = 0
definitePrime = []
for current in range(2, target):
    for test in range(2, int(sqrt(target))):
        if current % test == 0 and current != test:
            # print("test:", test, "and", current, "equals", test, "*", current / test, "therefore not prime")
            break
    else:
        addPrime(current)
        total = total + current
        print(current, "is a prime number", "total is:", total)
print()
print(definitePrime[10001])
# print(definitePrime[definitePrime.__len__() - 1], total)
