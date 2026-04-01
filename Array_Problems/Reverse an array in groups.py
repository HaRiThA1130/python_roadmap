def reverseInGroups(arr, k):
    i = 0
    n = len(arr)  
    while i < n:
        left = i
        # To handle case when k is not multiple of n
        right = min(i + k - 1, n - 1) 
        # reverse the sub-array [left, right]
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1  
        i += k
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8] 
    k = 3
    reverseInGroups(arr, k)
    print(" ".join(map(str, arr)))
