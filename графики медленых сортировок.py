import random
import time
import copy
import matplotlib.pyplot as plt


def bubble_sort(A):
    n=int(input())
    for j in range (n-1):
        for i in range (n-1-j):
            if A[i] > A[i + 1]:
                A[i],A[i + 1]=A[i + 1], A[i]
    return A


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A

def selection_sort(A):
    n = len(A)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]
    
    return A


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
    bubble_sort(m)
    time_finish = time.time()
    times_m.append(time_finish - time_start)

    time_start = time.time()
    insertion_sort(n)
    time_finish = time.time()
    times_q.append(time_finish - time_start)

    time_start = time.time()
    selection_sort(l)
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
