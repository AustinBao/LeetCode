def compress(n, lines):
    endString = ""
    for line in lines:
        previousCharacter = line[0] # assuming the line is not empty
        instancesOfCharacter = 0
        for character in line:
            if character == previousCharacter:
                instancesOfCharacter += 1
            else:
                endString += str(instancesOfCharacter) + " " + previousCharacter + " "
                instancesOfCharacter = 1
            previousCharacter = character
        endString += str(instancesOfCharacter) + " " + previousCharacter + "\n" # this is a newline character
    return endString

print(compress(4, ["+++===!!!!", "777777......TTTTTTTTTTTT", "(AABBC)", "3.1415555"]))
