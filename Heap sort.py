Heap sort

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):  
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):  
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

arr = [15, 3, 17, 10, 84, 19, 6, 22, 9]
heap_sort(arr)  # Sorts in-place
print("Sorted Array:", arr)

OUTPUT
Sorted Array: [3, 6, 9, 10, 15, 17, 19, 22, 84]

