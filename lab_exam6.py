def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index.")
        return arr
    else:
        del arr[index]
        return arr

# Test case
array = [3, 7, 1, 9, 4]
index_to_delete = 3

modified_array = delete_element(array, index_to_delete)
print(modified_array)


