'''
Bubble sort optimized implementation.
'''

from memory_profiler import profile


@profile
def bubble_sort_opt(arr: list) -> list:
    
    n = len(arr)

    for i in range(n):

        is_sorted = True
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
            
        if is_sorted:
            break
        
    return arr


# Test
test_arr = [55, 33, 14, 3, 1, -1, -2, -3, -4, -5]
sorted_arr = bubble_sort_opt(test_arr.copy())
print(f'Unsorted arr: {test_arr}')
print(f'Sorted arr: {sorted_arr}')
