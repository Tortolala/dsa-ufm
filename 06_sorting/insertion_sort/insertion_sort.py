'''
Insertion sort implementation.
'''


def insertion_sort(arr: list) -> list:

    n = len(arr)

    for i in range(1, n):
        
        j = i

        while (j > 0) and (arr[j - 1] > arr[j]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    
    return arr


# Test
test_arr = [55, 33, 14, 3, 1]
sorted_arr = insertion_sort(test_arr.copy())
print(f'Unsorted arr: {test_arr}')
print(f'Sorted arr: {sorted_arr}')




