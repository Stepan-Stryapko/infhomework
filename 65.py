n = int(input())
A = input().split()
k = 0
for i in A:
    if int(i) > 0:
        k += 1
print(k)
