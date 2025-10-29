def quicksort(arr):
    _quicksort(arr, 0, len(arr) -1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)

        _quicksort(arr, left, pi-1)
        _quicksort(arr,pi+1,right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    ## por que o python consegue comparar aquele array de arrays? ele faz da ESQUERDA para DIREITA
        #tupla1 = (5, 7, 3)
        #tupla2 = (7, 4, 2)
        #print(tupla1 < tupla2)  # Saída: True, porque 5 < 7
        #print(tupla1 > tupla2)  # Saída: False

        # Exemplo 2: Diferença no segundo elemento
        #tupla3 = (1, 5, 2)
        #tupla4 = (1, 4, 9)
        #print(tupla3 > tupla4)  # Saída: True, porque 5 > 4 (após o 1 ser igual)

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[right] = pivot, arr[i+1]

    return i+1



## Dado um target e uma lista, preciso retornar dois índices
## de números cujo a soma resulta no target
## target = 9
## nums = [2,7,11,15]
## return [0,1]

def two_sum(arr, target):
    # criar uma lista (val, index), do array que recebemos no parametro
    nums = []
    for idx,val in enumerate(arr):
        nums.append([val,idx]) # da esquerda pra direita...
    
    quicksort(nums)
    left = 0
    right = len(nums) -1

    while left <= right:
        current_sum = nums[left][0] + nums[right][0]
    # Esta ordenado em crescente. Se a soma ta maior diminui na tail, se ta menor aumenta no head
        if current_sum == target:
            return [nums[left][1],nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []





nums = [7,2,11,15]
print(two_sum(nums,9))