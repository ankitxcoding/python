def arraySort(arr, n):
    if n <= 1:
        return

    arraySort(arr, n - 1)
    elementInsert(arr, n - 1)


def elementInsert(arr, i):
    temp = arr[i]
    if i == 0 or temp > arr[i - 1]:
        arr.append(temp)
    else:
        


arr = list(map(int, input().split()))

arraySort(arr, len(arr))

print(arr)
