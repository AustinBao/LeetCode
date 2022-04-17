def parenthesesValid(str_of_parentheses):
    list_of_parentheses = []
    for items in str_of_parentheses:
        list_of_parentheses.append(items)

    parentheses_count = dict()
    for parentheses in list_of_parentheses:
        parentheses_count[parentheses] = parentheses_count.get(parentheses, 0) + 1

    if parentheses_count.get("(") != parentheses_count.get(")"):
        return False
    if parentheses_count.get("{") != parentheses_count.get("}"):
        return False
    if parentheses_count.get("[") != parentheses_count.get("]"):
        return False

    return True


print(parenthesesValid("(}"))

print(parenthesesValid("()[]{}"))
