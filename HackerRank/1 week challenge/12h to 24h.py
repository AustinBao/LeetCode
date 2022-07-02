list = "12:05:45PM"
list2 = "12:40:22AM"


def timeConversion(s):
    timelist = []
    for i in s:
        timelist.append(i)

    finalstrtime = ""
    if timelist[-2] == "P":
        if int(timelist[0]) * 10 + int(timelist[1]) == 12:
            finalstrtime += "12"
        else:
            finalstrtime += str(int(timelist[0]) * 10 + int(timelist[1]) + 12)

    else:
        if int(timelist[0]) * 10 + int(timelist[1]) == 12:
            finalstrtime += "00"
        else:
            return finalstrtime.join(timelist[:8])

    for elements in timelist[2:8]:
        finalstrtime += elements
    return finalstrtime


print(timeConversion(list))
print(timeConversion(list2))