def find_common_elements(arr1, arr2, arr3):
    # Initialize three pointers for each array
    ptr1 = ptr2 = ptr3 = 0
    result = []

    # Iterate until any of the pointers reaches the end of its respective array
    while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
        # If the current elements in all three arrays are equal, add it to the result
        if arr1[ptr1] == arr2[ptr2] == arr3[ptr3]:
            result.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        # If the current elements are not equal, increment the pointer of the smallest element
        else:
            min_val = min(arr1[ptr1], arr2[ptr2], arr3[ptr3])
            if arr1[ptr1] == min_val:
                ptr1 += 1
            if arr2[ptr2] == min_val:
                ptr2 += 1
            if arr3[ptr3] == min_val:
                ptr3 += 1

    return result
#DRiver code
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(find_common_elements(arr1, arr2, arr3))
