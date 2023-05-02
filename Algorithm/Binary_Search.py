n = int(input())
arr_n = list(map(int, input().split()))
arr_n.sort()
m = int(input())
arr_m = list(map(int, input().split()))
res = []
for i in range(m):
    lt = 0
    rt = n-1
    while lt <=rt:
        mid = (lt+rt)//2
        if arr_n[mid]<arr_m[i]:
            lt = mid + 1
        elif arr_n[mid]>arr_m[i]:
            rt = mid - 1
        else:
            res.append(1)
            break
    if lt > rt:
        res.append(0)
for i in res:
    print(i, end=' ')
    
#출처 : https://www.acmicpc.net/problem/10815
