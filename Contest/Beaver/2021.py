def CodeTranslator(code):
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
    binary = "".join(str_to_bin)
    return bool(binary == "1001001100010100010111000")


print(CodeTranslator("TAKECARE"))
