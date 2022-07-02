def thereyet(distances):
    c = [0]
    for i in range(0, 4):
        c.append(c[i] + distances[i])

    r = []
    for i in range(0, 5):
        for j in range(0, 5):
            distance = c[j] - c[i]
            if distance < 0:
                distance *= -1
            r.append(distance)
    return r


print(thereyet([3, 10, 12, 5]))

#     if len(distances) == 4:
#         start_distances = []
#         newlist = [0]
#         previous = 0
#         for i in distances:
#             newlist.append(previous + i)
#             previous += i
#         start_distances.append(newlist)
#     else:
#         start_distances = [distances]
#
#     result = calc(0, start_distances)
#     return result
#
#
# def calc(i, start_distances):
#     newlist = []
#     next_num = start_distances[i][i + 1]
#     for numbers_before in start_distances[i][:i + 1]:
#         newlist.append(numbers_before + next_num)
#     for numbers_before in start_distances[i][i + 1:]:
#         newlist.append(numbers_before - next_num)
#     start_distances.append(newlist)
#
#     return start_distances
