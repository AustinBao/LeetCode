def split(inputstr):
    inputList = []
    for i in inputstr:
        inputList.append(i)

    outerList = []
    maxValueOfJ = -1
    if len(inputList) == 1:
        return [inputList]

    for i in range(len(inputList)):
        if i > maxValueOfJ:
            innerList = [inputList[i]]
            for j in range(i + 1, len(inputList)):
                if inputList[i] == inputList[j]:
                    innerList.append(inputList[j])
                    maxValueOfJ = j
                else:
                    break
            outerList.append(innerList)

    return outerList

print(split("VXII"))