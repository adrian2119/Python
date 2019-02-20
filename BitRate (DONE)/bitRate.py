# Calculate the number of possible combinations in a string based on:
# the number of characters in the string and
# the number of possibilities for any 1 character


i = 0
k = 1
while i < 16: # 64-bit number
    k = k * 2
    i = i + 1
    print(i, len(str(k)), k)

