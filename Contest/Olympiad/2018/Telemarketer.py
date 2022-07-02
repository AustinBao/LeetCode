def telemarketer(phonenumber):
    fourdigit = []
    for i in str(phonenumber):
        fourdigit.append(i)

    if fourdigit[0] == "8" or "9":
        if fourdigit[1] == fourdigit[2]:
            if fourdigit[-1] == "8" or "9":
                return "ignore"
    return "answer"


print(telemarketer(8559))
print(telemarketer(8459))

