def ArrangeBooks(shelf):
    counter = 0

    # Turns str into list
    shelf_list = []
    for i in shelf:
        shelf_list.append(i)

    # breaks code into subsection. section between first L and the end. ex: LL[...]  ... = this section
    medium_and_small = []
    for index, elements in enumerate(shelf_list):
        if elements == "M" or elements == "S":
            medium_and_small = shelf_list[index::]
            break

    # checks medium and small list for L's. Finds the sub section of all elements until the first L
    sub_list = []
    for index, value in enumerate(medium_and_small):
        sub_list.append(value)
        if value == "M":
            counter += 1
            continue
        if value == "L":
            break

    # pops the start of the sublist in order to imitate "swapping"
    smaller_sub = []
    for i in range(0, counter):
        smaller_sub.append(sub_list.pop(0))

    # after pop list is the values popped just before hitting the first L and how it would look if rearranged correctly
    after_pop_list = []
    for value in sub_list[:-1]:
        after_pop_list.append(value)
    for i in smaller_sub:
        after_pop_list.append(i)

    # finds the index of the L books in the shelf
    index_of_large = []
    for index, value in enumerate(medium_and_small):
        if value == "L":
            index_of_large.append(index)
    # gives the last L book in the medium and small list
    last_large_index = max(index_of_large)
    # gives all elements following the last L book in the medium and small list
    ele_after_large = medium_and_small[last_large_index + 1:]

    # creation of the TRUE medium and small list
    true_m_and_s = []
    if len(ele_after_large) == 0:
        true_m_and_s = after_pop_list
    else:
        for i in range(0, counter):
            medium_and_small.pop(0)
        for value in after_pop_list:
            medium_and_small.insert(last_large_index, value)
        true_m_and_s = medium_and_small[last_large_index:]

    # finds the start of the small books
    small_books = []
    for index, value in enumerate(true_m_and_s):
        if value == "S":
            small_books = true_m_and_s[index:]
            break
        else:
            continue

    # counts the "swaps" between medium and small books
    small_counter = 0
    medium_counter = 0
    for elements in small_books:
        if elements == "S":
            small_counter += 1
        elif elements == "M":
            medium_counter += 1

    counter += min(medium_counter, small_counter)

    return counter


print(ArrangeBooks("LLMMSLL"))

print(ArrangeBooks("LLMMSLLLMLLLMSMS"))

print(ArrangeBooks("LMLLLMSMS"))
