haystack = "helo"
needle = ""

def haystackindex(stack, needle):
    if len(needle) == 0:
        return 0
    for i in range(len(stack)):
        if stack[i:i+len(needle)] == needle:
            return i
    return -1

user1 = haystackindex(haystack,needle)
print(user1)