def maxProduct(arr):
    arr.sort()
    n = len(arr)
    # case 1: 3 largest
    prod1 = arr[n-1] * arr[n-2] * arr[n-3]
    # case 2: 2 smallest + largest
    prod2 = arr[0] * arr[1] * arr[n-1]
    return max(prod1, prod2)
# input
arr = list(map(int, input().split()))
print(maxProduct(arr))
