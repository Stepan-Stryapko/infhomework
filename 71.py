n = int(input())
A = input().split()
N = A[1::] + [A[0]]
print(*N)
