def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j] # bring the back element to front
            j -= 1 # compare the last element
        arr[j+1] = key # bring to key to the smaller slot
        print(arr)
arr = [64, 34, 25, 12, 22, 11, 90]

insertionSort(arr)
print("Sorted arr is:",arr)

# https://www.geeksforgeeks.org/insertion-sort/