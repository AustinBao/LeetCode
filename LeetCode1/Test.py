code = "TEACRATE"

dictionary = {
        "T": "1",
        "E": "00",
        "A": "0010",
        "K": "0110",
        "C": "1010",
        "R": "1110",
    }
str_to_bin = []
for i in code:
    str_to_bin.append(dictionary[i])
    print(str_to_bin)