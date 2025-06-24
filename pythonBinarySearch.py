def binarySearch(arr, x):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


n, x = map(int, input().split())
arr = list(map(int, input().split()))[:n]

ans = binarySearch(arr, x)
print(ans)
