#Dynamic Programming 피보나치 수열 비교

#Memoiztion : Top-Down 가끔 재귀 횟수 제한 오류가 걸릴 수도 있음
'''
import time

d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for num in range(5, 6):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')
'''

#DP Table : Bottom-Up
'''
d = [0] * 100
d[1] = 1
d[2] = 1
N = 99 #피보나치 수열의 99번째 숫자는?

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])

#출처 https://techblog-history-younghunjo1.tistory.com/183
