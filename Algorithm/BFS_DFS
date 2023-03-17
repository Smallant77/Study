from collections import deque

def bfs(start, graph):
    dq = deque([start])
    visited = []
    while dq:
        now = dq.popleft()
        if now not in visited:
            visited.append(now)
            for i in gr[now]:
                if i not in visited:
                    dq.append(i)
    return visited

def dfs(start, graph):
    dq = deque([start])
    visited = []
    while dq:
        now = dq.pop()
        if now not in visited:
            visited.append(now)
            for i in gr[now]:
                if i not in visited:
                    dq.append(i)
    return visited
        
gr = [
    [],[2, 3, 8],[1, 7],[1, 4, 5],[3, 5],[3, 4],[7],[2, 6, 8],[1, 7]
]

for i in bfs(1,gr):
    print(i, end=' ')
print()
for i in dfs(1,gr):
    print(i, end=' ')

참고 : https://freedeveloper.tistory.com/373
