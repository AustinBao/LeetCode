motel = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
minimum = int(input())
maximum = int(input())
extramotels = list(input())

for motels in extramotels:
    if motels == ",":
        continue
    else:
        motel.append(int(motels))

motel.sort()

def TruckRoutes(min, max, motels):
    possibilities = {}
    for curr_stop in range(0, len(motels) - 1):
        for next_stop in range(curr_stop + 1, len(motels)):
            if max >= motels[next_stop] - motels[curr_stop] >= min:
                possibilities[motels[curr_stop]] = motels[next_stop]
            else:
                continue
    return possibilities


print(TruckRoutes(minimum, maximum, motel))