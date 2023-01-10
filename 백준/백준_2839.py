#설탕배달
#import sys
#sys.setrecursionlimit(10**5)
cache=[-1]*10000
def solve(n):
    if n==0:return 0
    if n<0: return 5000
    if cache[n]!= -1:
        return cache[n]
    cache[n] = min(solve(n-3),solve(n-5))+1
    return cache[n]
n = int(input())
a = solve(n)
if a>=5001:
    print("-1")
else:
    print(solve(n))