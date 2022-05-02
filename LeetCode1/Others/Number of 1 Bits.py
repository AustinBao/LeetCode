def countOneBits(string_of_bits):
    j = 0
    for i in string_of_bits:
        if int(i) == 1:
            j += 1
    return j


print(countOneBits("11111111111111111111111111111101"))
print(countOneBits("00000000000000000000000010000000"))
