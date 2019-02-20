# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?

penNumbers = []
total = 0
penAdd = []
penSub = []
pen = 0
i = 1
add = 0
sub = 0
while i <= 3000:
    pen = int(i * ((3 * i - 1) / 2))
    penNumbers.append(pen)
    i = i + 1

print(penNumbers)

i = penNumbers.__len__() - 1
j = 0
while i >= penNumbers.__len__() / 2:
    # print(i)
    sub = 0
    while j <= penNumbers.__len__() / 2:
        add = (penNumbers[i] + penNumbers[j])
        if add <= penNumbers[len(penNumbers) - 1]:
            # print(i, j, penNumbers[i], penNumbers[j], add, sub, penNumbers[len(penNumbers) - 1])

            if penNumbers.__contains__(add):
                sub = (penNumbers[i] - penNumbers[j])
                if sub > 0:
                    # print(i, j, penNumbers[i], penNumbers[j], add, sub, penNumbers[len(penNumbers) - 1])
                    if penNumbers.__contains__(sub):
                        print("-------------------------",penNumbers[i], penNumbers[j], add, sub)
        j = j + 1
    j = 0
    i = i - 1

# i = 0
# j = 0
# while i < penAdd.__len__():
#     while j < penSub.__len__():
#         if penAdd.__contains__(penSub[j]):
#             print(penAdd[i], penSub[j])
#         j = j + 1
#     j = 0
#     i = i + 1