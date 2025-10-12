def reverse_quicksort(arr):
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
        if arr[j] > pivot: ## reverse...
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

# Reverse Quicksort implementation above

## Linear
def h_index_linear(arr):
    h = 0
    for i in range(len(arr)):
        if arr[i] >= i+1:
            h += 1
        else:
            return h
        
## Binary
def h_index_binary(arr):
    left = 0
    right = len(arr) - 1
    h = 0 
    while left <= right:
        mid = (left + right) // 2
        qt_art = mid + 1
        if arr[mid] >= qt_art:
            h = qt_art
            left = mid + 1
        else:
            right = mid - 1
    return h


citations = [5, 3, 10, 8, 4]
reverse_quicksort(citations) # [10, 8, 5, 4, 3]
print(h_index_linear(citations))
print(h_index_binary(citations))