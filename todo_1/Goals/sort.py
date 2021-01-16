
def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            key = A[i]
            A[i] = A[j]
            A[j] = key
            i += 1 
    key = A[i]
    A[i] = A[r]
    A[r] = key
    return i

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def QuickSort(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr