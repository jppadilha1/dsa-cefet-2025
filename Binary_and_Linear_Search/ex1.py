def quicksort(arr):
    _quicksort(arr, 0, len(arr)-1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr,left,right)

        _quicksort(arr, pi+1, right)

        _quicksort(arr,0, pi-1)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

# Quicksort implementation above

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    ## Minha solução, para retornar a posição em que o número deveria estar inserido
    position = 0
    for i in range(len(arr)):
        if arr[i] <= target:
            position += 1
    return position

# Binary Search
def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1
    

nums = [2, 0, 3, 1, 1, 0]
quicksort(nums) # [0, 0, 1, 1, 2, 3] 
print(linear_search(nums,3))
print(binary_search(nums,2))


