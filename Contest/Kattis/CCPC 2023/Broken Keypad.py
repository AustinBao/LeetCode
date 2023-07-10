rng = list(input())

start_lst = rng[0]
end_lst = rng[-1]

for i in range(len(rng)):
    if rng[i] == " ":
        start_lst = rng[:i:]
        end_lst = rng[i + 1::]

end_str = ""
for i in end_lst:
    end_str += i

start_str = ""
for i in start_lst:
    start_str += i

start_int = int(start_str)
end_int = int(end_str)
seven_counter = 0
list_of_digits = []

for num in range(start_int, end_int + 1):
    for digits in str(num):
        list_of_digits.append(digits)


for num in list_of_digits:
    if int(num) == 7:
        seven_counter += 1


