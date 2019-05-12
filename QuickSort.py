import random


def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p, r)


def Quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_partition(A, p, q-1)
        randomized_partition(A, q+1, r)


list1 = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
Quicksort(list1, 0, len(list1)-1)
print(list1)
