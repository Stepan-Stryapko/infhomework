def dfs(a, n):
    global visited
    print(f"in {n}")
    
    for i in range(len(a[n])):
        if a[n][i] in visited:
            pass
        else:
            visited.append(a[n][i])
            
            dfs(a, a[n][i])
    
    print(f"out of {n}")

n, m = map(int, input().split())
g = {}
for i in range(m):
    b = list(map(int, input().split()))
    if b[0] not in g:
        g[b[0]] = []
    if b[1] not in g:
        g[b[1]] = []
    g[b[0]].append(b[1])
    g[b[1]].append(b[0])
print(g)
print("\n\n\n")
visited = [0]
dfs(g, 0)
