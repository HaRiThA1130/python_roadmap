def pushZerosToEnd(arr):
    j = 0  # position for next non-zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

# take input
arr = list(map(int, input().split()))

# function call
pushZerosToEnd(arr)

# print output
for x in arr:
    print(x, end=" ")
