def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

#test case
array = ['b','z', 'd', 'a', 'c', 'f', 'e','r']
bubblesort(array)
print("Sorted array:", array)








