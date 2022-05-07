def harpTuning(instructions):
    list_of_words = []
    for i in instructions:
        list_of_words.append(i)

    for elements in range(0, len(list_of_words)):

        if list_of_words[elements] == "+":
            list_of_words.pop(elements)
            list_of_words.insert(elements, "tighten")

        elif list_of_words[elements] == "-":
            list_of_words.pop(elements)
            list_of_words.insert(elements, "loosen")

    str1 = " "
    return str1.join(list_of_words)


print(harpTuning("ABD+4FCD-5YUWZX+1"))
