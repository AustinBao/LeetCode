def check_if_desired_value_in_loop(list_of_nodes, desired_node):
    current_index = 0
    while list_of_nodes[current_index] is not desired_node:
        current_index += 1

    output_list = list_of_nodes[current_index:]
    return output_list


list_of_n = [1, 2, 3, 1]
me = check_if_desired_value_in_loop(list_of_n, 1)
print(me)


