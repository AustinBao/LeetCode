items = ["(", ")", "[", "]", "{", "}"]

counts = dict()
for i in items:
    counts[i] = counts.get(i, 0) + 1

print(counts.get("["))