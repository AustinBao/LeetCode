def shapes(S, R):
    if (S * S) > (3.14 * R * R):
        return "SQUARE"
    else:
        return "CIRCLE"
print(shapes(12,124))