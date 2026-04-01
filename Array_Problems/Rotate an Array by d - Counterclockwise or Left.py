arr = list(map(int, input().split()))
d = int(input())

d = d % len(arr)   # handle large d

arr = arr[d:] + arr[:d]

print(*arr)
