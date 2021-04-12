nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def rotateImage(matrix):
    n = len(matrix[0])
    # n is the number of items in our nested array (in our case its 3 cause each nested array has 3 elements)
    for rows in range(n):
        # rows are the index of rows in our matrix (this would give us 0,1, and 2)
        for col in range(rows, n):
            # col gives us each iterations index for the columbs (returns, 0,1,2 then 1,2 then 2)
            matrix[col][rows], matrix[rows][col] = matrix[rows][col], matrix[col][rows]
    #         switches the number in the specific index of the row with the columbs

    for i in range(n):
        matrix[i].reverse()
    #     reverses the list so we get our answer (try it without and see what it returns)
    return matrix


test = rotateImage(nums)
print(test)