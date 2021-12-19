def heapify(arr, n, i): 
    larg = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[l] > arr[larg]: 
        larg = l
 
    if r < n and arr[r] > arr[larg]: 
        larg = r


    if larg != i: 
        arr[i], arr[larg] = arr[larg], arr[i]
        heapify(arr, n, larg)


def build_heap(arr, n): 
    startIdx = n // 2 - 1

    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)



arr = list(map(int, input().split()))

n = len(arr)

build_heap(arr, n) 

print(" ".join(map(str, arr))) 
