# https://www.ualberta.ca/computing-science/media-library/outreach/iverson/iverson2018solutions.pdf


def compress(string):
    text = []
    for i in string:
        text.append(i)

    sublist = []
    previous = text[0]
    start = 0
    for index, letter in enumerate(text):
        if letter == previous:
            continue
        elif letter != previous:
            sublist.append(text[start:index])
            previous = letter
            start = index
    sublist.append(text[start:])

    count = []
    for sublists in sublist:
        count.append(len(sublists))

    final = []
    for index, num in enumerate(count):
        if num <= 2:
            final.append(sublist[index])
            continue
        else:
            final.append(str(count[index]))
            final.append(sublist[index])

    output = []
    for elements in final:
        for letters in elements:
            output.append(letters)
    outputstr = ""
    return outputstr.join(output)


print(compress("cccccccaaacccccaaa"))
print(compress("abbabbaabbbaba"))
