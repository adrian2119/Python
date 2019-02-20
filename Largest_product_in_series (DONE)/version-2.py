#
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

counter = 1
answer = 0
possible = 5
target = 100
# answer = 67017420985
# possible = 1350002
# target = 1360000

index = 0
inTheArray = True

while possible < target:
    while counter <= possible:
        while possible % counter == 0:
            if counter <= (possible / 2) and counter > 1:
                print possible, "devided by", counter, "is", possible / counter, "remainder", possible % counter,
                index = 4
                possible = possible + 1
            elif counter == 1:
                print possible, "is devisible by one"
                index = index + 1
                counter = counter + 1
            else:
                print possible, "is prime"
                index = 0
                counter = counter + 1
                possible = possible + 1
        counter = 1

        # while counter <= (possible / 2):
            # if counter == 1:
            #     print possible, "is devisible by one"
            # elif possible % counter == 0:
            #     counter = 1
            # elif counter > (possible / 2):
            #     print possible, "is not devisible by anything in the first half"
            #     counter = 1
            #     possible = possible + 1
        #     counter = counter + 1
        #     possible = possible + 1
        # counter = counter + 1
print
print "Answer:", answer, "Possible:", possible
print
print "answer =", answer
print "possible =", possible
print "target =", target + 10000
