# https://www.cemc.uwaterloo.ca/contests/computing/2021/ccc/juniorEF.pdf


def ArrangeBooks(shelf):
    counter = 0

    shelf_list = []
    for book in shelf:
        shelf_list.append(book)

    subsections = {}
    for item in shelf_list:
        if item in subsections:
            subsections[item] += 1
        else:
            subsections[item] = 1

    large_range = range(0, subsections["L"])
    medium_range = range(subsections["L"], subsections["L"] + subsections["M"])
    small_range = range(subsections["L"] + subsections["M"], subsections["L"] + subsections["M"] + subsections["S"])

    for l_index in large_range:
        if shelf_list[l_index] != "L":
            for m_index in medium_range:
                if shelf_list[m_index] == "L":
                    counter += 1
                    shelf_list.pop(m_index)
                    shelf_list.insert(m_index, shelf_list[l_index])
                    shelf_list.pop(l_index)
                    shelf_list.insert(l_index, "L")
                    continue

            for s_index in small_range:
                if shelf_list[s_index] == "L":
                    counter += 1
                    shelf_list.pop(s_index)
                    shelf_list.insert(s_index, shelf_list[l_index])
                    shelf_list.pop(l_index)
                    shelf_list.insert(l_index, "L")
                    continue

    for m_index in medium_range:
        if shelf_list[m_index] != "M":
            for s_index in small_range:
                if shelf_list[s_index] == "M":
                    counter += 1
                    shelf_list.pop(s_index)
                    shelf_list.insert(s_index, "S")
                    shelf_list.pop(m_index)
                    shelf_list.insert(m_index, "M")

    return counter


print(ArrangeBooks("LLMMSLL"))

print(ArrangeBooks("LLMMSLLLMLLLMSMS"))

print(ArrangeBooks("LMLLLMSMS"))
