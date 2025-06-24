def sortStack(stack):
    if len(stack) <= 1:
        return stack

    temp = stack[-1]  # or simply do stack.pop() here instead of next line.
    stack.pop()
    sortStack(stack)
    insertArray(stack, temp)


def insertArray(stack, temp):
    if len(stack) == 0 or stack[-1] <= temp:
        stack.append(temp)
        return

    x = stack[-1]  # or simply do stack.pop() here instead of next line.
    stack.pop()
    insertArray(stack, temp)
    stack.append(x)
    return


stack = list(map(int, input().split()))

sortStack(stack)

print(stack)
