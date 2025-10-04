def quicksort(arr):
    _quicksort(arr,0,len(arr)-1)

def _quicksort(arr, left, right):
    if left < right: ## pelomenos 2 elementos no range passado.
        pi = partition(arr,left,right) 

        _quicksort(arr,0, pi-1) #recursiva pra esquerda do pivo

        _quicksort(arr,pi+1,right) #recursiva pra direita do pivo



def partition(arr, left, right) -> int: ## Retorna sempre a posição do pivo
   pivot = arr[right]
   i = left - 1 #ponteiro de referência. representa todos a esquerda e o return

   for j in range(left,right):
       if arr[j] <= pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]

   arr[i+1], arr[right] = pivot, arr[i+1]
   return i + 1


nums = [2, 0, 3, 1, 1, 0]
quicksort(nums)
print(nums)