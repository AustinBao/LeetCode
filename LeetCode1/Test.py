our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
chunked_list = list()
chunk_size = 3
for i in range(0, len(our_list), chunk_size):
    chunked_list.append(our_list[i:i+chunk_size])
print(chunked_list)
# Returns: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]