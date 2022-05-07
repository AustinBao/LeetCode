def fergusonball(separate_players, scores_and_fouls):
    if separate_players == 0:
        return "0-"

    sublist = []
    for nums in range(0, len(scores_and_fouls), 2):
        sublist.append(scores_and_fouls[nums:nums + 2])

    star_players = []
    for i in sublist:
        for j in range(0, len(sublist[0]) - 1):
            star_players.append((i[j] * 5) - (i[j + 1] * 3))

    counter = 0
    for items in star_players:
        if items > 40:
            counter += 1

    if counter == separate_players:
        return "{}+".format(counter)
    else:
        return "{}-".format(counter)


print(fergusonball(4, [12, 4, 10, 3, 9, 1, 18, 2]))

print(fergusonball(0, []))

print(fergusonball(1, [9, 1]))
