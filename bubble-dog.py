def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size-i-1): ##-i pra não percorrer os últimos
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

lista = [10,15,2,3,5,12,1,7,8,9]
bubble_sort(lista)
print(lista)