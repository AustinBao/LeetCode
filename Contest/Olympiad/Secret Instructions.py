def secretInstructions1(code):
    int_to_list = []
    for elements in str(code):
        int_to_list.append(int(elements))

    previous_direction = ""
    final_instructions = []
    all_ecompassing_list = chunkList1(int_to_list)

    for sub_list in all_ecompassing_list:

        # edge case when code = 99999
        if sub_list == [9, 9, 9, 9, 9]:
            all_ecompassing_list.pop(-1)
            continue

        # edge case when code starts with two 0's
        sum_first_two_nums = sub_list[0] + sub_list[1]
        if sum_first_two_nums == 0:
            final_instructions.append(previous_direction)
            final_instructions.append(''.join(str(elements) for elements in sub_list[2:]))
            continue

        # used for normal codes
        remainder_of_sum = (sub_list[0] + sub_list[1]) % 2
        if remainder_of_sum == 0:
            final_instructions.append("right")
            final_instructions.append(''.join(str(elements) for elements in sub_list[2:]))
            previous_direction = "right"
        else:
            final_instructions.append("left")
            final_instructions.append(''.join(str(elements) for elements in sub_list[2:]))
            previous_direction = "left"

    command = ' '.join(str(elements) for elements in final_instructions)

    return command


def chunkList1(code_list):
    chunked_list = []
    for items in range(0, len(code_list), 5):
        chunked_list.append(code_list[items:items + 5])
    return chunked_list


print(secretInstructions1(57234009073410099999))
print(secretInstructions1(99999))
print(secretInstructions1(123456789099999))



