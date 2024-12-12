import random
import time
import copy
import matplotlib.pyplot as plt


def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    res += A[i:] + B[j:]
    return res


def mergesort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    return merge(mergesort(left), mergesort(right))


def qsort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left >= right:
        return
    i = left
    j = right
    pivot = A[left]
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, left, j)
    qsort(A, i, right)


def heap_add(A, value):
    A.append(value)
    i = len(A) - 1
    while i > 0 and A[i] > A[(i - 1) // 2]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2


def heap_pop(A):
    res = A[0]
    if len(A) == 1:
        return res
    A[0] = A.pop()
    i = 0
    j = 2 * i + 1
    k = 2 * i + 2
    while j < len(A):
        c = j
        if k < len(A) and A[j] < A[k]:
            c = k
        if A[i] < A[c]:
            A[i], A[c] = A[c], A[i]
            i = c
        else:
            break
        j = 2 * i + 1
        k = 2 * i + 2
    return res


def heap_sort(A):
    heap = []
    for element in A:
        heap_add(heap, element)
    for i in range(len(A)):
        A[len(A) - 1 - i] = heap_pop(heap)


sizes = []
times_m = []
times_q = []
times_h = []
for i in range(100):
    sizes.append(1000 * i)
for sample in sizes:
    m = [random.randrange(10**6) for k in range(sample)]
    n = copy.copy(m)
    l = copy.copy(m)
    time_start = time.time()
    cache = mergesort(m)
    time_finish = time.time()
    times_m.append(time_finish - time_start)

    time_start = time.time()
    qsort(n)
    time_finish = time.time()
    times_q.append(time_finish - time_start)

    time_start = time.time()
    heap_sort(l)
    time_finish = time.time()
    times_h.append(time_finish - time_start)


fig = plt.figure()
ax = fig.add_subplot()
ax.set_facecolor("white")
ax.plot(sizes, times_m, "black", label="merge")
ax.plot(sizes, times_q, "red", label="quick")
ax.plot(sizes, times_h, "blue", label="heap")
plt.xlabel("data size")
plt.ylabel("time, s")
plt.legend()
plt.savefig("quick sortings comparison.png", dpi=300)
plt.show()
