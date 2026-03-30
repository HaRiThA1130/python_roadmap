def thirdLargest(arr):
    n = len(arr)
    
    # Sort the array 
    arr.sort()
    
    # Return the third largest element 
    return arr[n - 3]

if __name__ == "__main__":
    arr = [1, 14, 2, 16, 10, 20]
    print(thirdLargest(arr))
