def goodGroups(num_tog, tog, num_sep, sep, num_group, groups):
    counter = 0
    for indi_groups in groups:
        if together(indi_groups, tog) is False:
            counter += 1
        if separate(indi_groups, sep) is False:
            counter += 1

    return counter


def together(group, tog):
    for inseparatable in tog:
        for index2, student in enumerate(inseparatable):
            if student in group:
                if index2 == 1:
                    if inseparatable[0] not in group:
                        return False
                    if inseparatable[0] in group:
                        break
                else:
                    if inseparatable[1] not in group:
                        return False
                    if inseparatable[1] in group:
                        break
    return True


def separate(group, sep):
    for separated in sep:
        for index2, name in enumerate(separated):
            if name in group:
                if index2 == 1:
                    if separated[0] in group:
                        return False
                    if separated[0] not in group:
                        break
                else:
                    if separated[1] in group:
                        return False
                    if separated[1] not in group:
                        break
    return True


print(goodGroups(3, [["A", "B"], ["G", "L"], ["J", "K"]], 2, [["D", "F"], ["D", "G"]], 4,
                 [["A", "C", "B"], ["P", "O", "Y"], ["E", "H", "I"], ["J", "K", "Z"]]))


print(goodGroups(3, [["A", "B"], ["G", "L"], ["J", "K"]], 2, [["D", "F"], ["D", "G"]], 4,
                 [["A", "C", "G"], ["B", "D", "F"], ["E", "H", "I"], ["J", "K", "L"]]))
1