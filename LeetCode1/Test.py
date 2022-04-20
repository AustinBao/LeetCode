next_row = []
a_list = [1,1]
a_list.insert(0, 0)
a_list.insert(len(a_list), 0)

for i in range(0, len(a_list) - 1):
    j = i + 1
    next_row.append(a_list[i] + a_list[j])

actual = [next_row]
print(actual)