def decompress(enc):
    at = 0
    output = ""

    while at < len(enc):
        char_pos = at
        # read off the digits starting at position "at"
        while enc[char_pos].isdigit():
            char_pos += 1
        if char_pos == at:
            # if we read no digits, use a single character
            num = 1
        else:
            # else, get the number
            num = int(enc[at:char_pos])
        # either way, the character is at index char_pos
        output += enc[char_pos] * num
        at = char_pos + 1

    return output


print(decompress("7ccccccc3aaa5ccccc3aaa"))
print(decompress("abbabbaa3bbbaba"))
