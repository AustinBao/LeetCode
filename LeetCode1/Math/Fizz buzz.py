
def countPrime(num):
    for i in range(1, num+1):
        for j in range(2,9):
            if i % j == 0:
                print(i)


mynum = 10
me = countPrime(mynum)
print(me)