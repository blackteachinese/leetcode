def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print("Sorted arr is:",arr)

# https://www.geeksforgeeks.org/bubble-sort/

# https://www.softwaretestinghelp.com/coding-interview-questions/