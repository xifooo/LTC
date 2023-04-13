def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    return i

def selection_sort(A, i = None):
    if i is None: i = len(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i], A[j] = A[j], A[i]
        selection_sort(A, i-1)
        
def merge_sort(A):
    ...

def merge():
    ...

A = [84, 67, 79, 30, 44, 27, 63, 7, 41, 53, 8, 20, 11, 26, 35, 15, 39, 69]
selection_sort(A)
print(A)