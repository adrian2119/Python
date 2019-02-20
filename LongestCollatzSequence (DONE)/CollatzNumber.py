# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

issue = [837799, 2513398, 1256699, 3770098, 1885049, 5655148, 2827574, 1413787, 4241362, 2120681, 6362044, 3181022, 1590511, 4771534, 2385767, 7157302, 3578651, 10735954, 5367977, 16103932, 8051966, 4025983, 12077950, 6038975, 18116926, 9058463, 27175390, 13587695, 40763086, 20381543, 61144630, 30572315, 91716946, 45858473, 137575420, 68787710, 34393855, 103181566, 51590783, 154772350, 77386175, 232158526, 116079263, 348237790, 174118895]

n = 0
j = 1
chainLength = 0
while j <= 1000000:
    n = j
    numbers = []
    # print(j)
    while n <= 5000000000000000: # The answer gets the value of n to a stupidly big number !!
        # n = n + 1
        # n = i
        if n == 1:
            numbers.append(1)
            # print(numbers)
            break
        elif n % 2 == 0:
            numbers.append(n)
            n = int(n / 2)
            # print(n, "divided by", 2, "is: ", n / 2)
        elif n % 2 == 1:
            numbers.append(n)
            n = (3 * n) + 1
            # print(n, "multiplied by 3 is: ", n * 3, "add 1 is: ", (n * 3) + 1)

    if numbers.__len__() >= chainLength:
        print()
        # print("j",j, "n", n, "length",numbers.__len__(), "chain",chainLength, "first", numbers[0])
        chainLength = numbers.__len__()
        print("j", j, "length", numbers.__len__(), numbers[numbers.__len__() - 1], numbers)
    j = j + 1

