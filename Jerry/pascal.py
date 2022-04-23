def pascalTriangle(existingRows, n):
    currentRow = len(existingRows)
    if currentRow == n:
        return existingRows
    else:
        newRow = [1]
        previousRow = existingRows[-1]
        for index, number in enumerate(previousRow):
            if len(previousRow) == index + 1:
                continue
            else:
                nextNumber = previousRow[index + 1]
                newRow.append(number + nextNumber)
        newRow.append(1)
        existingRows.append(newRow)
        return pascalTriangle(existingRows, n)


def pascal(n):
    return pascalTriangle([[1]], n)


if __name__ == '__main__':
    print(pascal(1))
    print(pascal(2))
    print(pascal(3))
    print(pascal(4))
    print(pascal(5))
    print(pascal(6))
