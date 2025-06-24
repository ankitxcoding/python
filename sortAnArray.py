def sortArray(arr):
    if len(arr) <= 1:
        return arr

    temp = arr[len(arr) - 1]  # or simply do arr.pop() here instead of next line.
    arr.pop()
    sortArray(arr)
    insertArray(arr, temp)


def insertArray(arr, temp):
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:  # arr[-1] <= temp
        arr.append(temp)
        return

    x = arr[len(arr) - 1]  # or simply do arr.pop() here instead of next line.
    arr.pop()
    insertArray(arr, temp)
    arr.append(x)
    return


arr = list(map(int, input().split()))

sortArray(arr)

print(arr)
