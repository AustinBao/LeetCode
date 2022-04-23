def parenthesesValid(str_of_parentheses):
    list_of_parentheses = []
    for items in str_of_parentheses:
        list_of_parentheses.append(items)

    op_brackets = list_of_parentheses[0::2]
    cl_brackets = list_of_parentheses[1::2]
    if len(op_brackets) != len(cl_brackets):
        return False
    else:
        index = 0
        while index != len(op_brackets):
            if op_brackets[index] == "(":
                if cl_brackets[index] != ")":
                    return False
            if op_brackets[index] == "[":
                if cl_brackets[index] != "]":
                    return False
            if op_brackets[index] == "{":
                if cl_brackets[index] != "}":
                    return False
            index += 1
    return True


print(parenthesesValid("("))
print(parenthesesValid("(}"))
print(parenthesesValid("({)}"))
print(parenthesesValid("(){}"))
print(parenthesesValid("(){}[][][](){}{)"))

