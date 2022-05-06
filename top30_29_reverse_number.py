# original number 12345
# reversed number 54331

def reverseNum(original):
    reversed = 0
    while original > 0:
        reversed *= 10
        reversed += original % 10
        original //= 10
        # print(original,reversed)
    return reversed

print(reverseNum(12345))