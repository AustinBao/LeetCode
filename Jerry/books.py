def solve(books):
    lSize = books.count("L")
    mSize = books.count("M")

    lChunk = books[0: lSize]
    mChunk = books[lSize: lSize + mSize]
    sChunk = books[lSize + mSize:]

    numberOfSwaps = 0

    for book in lChunk:
        if book == "M":
            if mChunk.__contains__("L"):
                pos = mChunk.index("L")
        #if book == "S":



    return numberOfSwaps

print(solve("LLSMS"))