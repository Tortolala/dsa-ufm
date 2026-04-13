'''
Bubble sort basic implementation.
'''

from memory_profiler import profile


@profile
def bubble_sort(arr: list) -> list:
    
    n = len(arr)

    for _ in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
    return arr

# Test
test_arr = [55, 33, 14, 3, 1, -1, -2, -3, -4, -5]
sorted_arr = bubble_sort(test_arr.copy())
print(f'Unsorted arr: {test_arr}')
print(f'Sorted arr: {sorted_arr}')
