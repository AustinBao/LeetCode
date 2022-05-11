def harpTuning(instructions):
    tunedlist = []
    for elements in instructions:
        if elements == "+":
            tunedlist.append("tighten")
            continue
        if elements == "-":
            tunedlist.append("loosen")
            continue
        tunedlist.append(elements)

    substrings = ""
    listofstrings = []
    for i in tunedlist:
        if i == "tighten" or i == "loosen":
            listofstrings.append(substrings)
            substrings = ""
        if i.isalpha():
            if len(i) == 1:
                substrings += i
        else:
            continue

    listoftuning = []
    for i in tunedlist:
        if i == "tighten":
            listoftuning.append("tighten")
        if i == "loosen":
            listoftuning.append("loosen")

    listofnumbers = []
    for i in tunedlist:
        if i.isdigit():
            listofnumbers.append(i)
        else:
            continue

    final = []
    for index in range(0, len(listofstrings)):
        final.append("{} {} {}".format(listofstrings[index], listoftuning[index], listofnumbers[index]))

    str1 = " "
    return str1.join(final)


print(harpTuning("ABD+4FCD-5YUWZX+1TRADOP-2"))
