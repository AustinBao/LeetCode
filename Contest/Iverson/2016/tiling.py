def tiling_sol1(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


def tiling_sol2(n):
    f = [1, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


print(tiling_sol2(4))
# print(tiling_sol1(1000))
