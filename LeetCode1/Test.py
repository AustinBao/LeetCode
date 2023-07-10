number_of_people = int(input())
days_available = []

for people in range(number_of_people):
    days_available.append(input())

best_days = []
count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for schedule in days_available:
    for day in range(len(schedule)):
        if schedule[day] == "Y":
            count[day + 1] += 1

maximum = 0
for key in count:
    if count[key] > maximum:
        maximum = count[key]

for key in count:
    if count[key] == maximum:
        best_days.append(str(key))

print(",".join(best_days))
