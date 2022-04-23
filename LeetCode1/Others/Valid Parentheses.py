def parenthesesValid(str_of_parentheses):
    list_of_parentheses = []
    for items in str_of_parentheses:
        list_of_parentheses.append(items)
    if len(list_of_parentheses) % 2 != 0:
        return False
    else:
        quick_list = [list_of_parentheses[0]]
        for index,value in enumerate(str_of_parentheses):
            if quick_list[index] != value:
                quick_list.append(value)

print(parenthesesValid("("))
print(parenthesesValid("(}"))
print(parenthesesValid("({)}"))
print(parenthesesValid("(){}"))
print(parenthesesValid("({})"))
print(parenthesesValid("{{}[][[[]]]}"))
