def secretInstructions(sec_code):
    int_to_list = []
    for elements in str(sec_code):
        int_to_list.append(elements)

    chunked_list = []
    for i in range(0, len(int_to_list), 5):
        chunked_list.append(int_to_list[i:i + 5])
    print(chunked_list)


print(secretInstructions(5723400907))


