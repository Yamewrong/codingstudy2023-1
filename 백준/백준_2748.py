num=[]
cache=[-1]*10000
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if cache[n]!= -1:
        return cache[n]
    cache[n] = fibo(n-1)+fibo(n-2)
    return cache[n]
n = int(input())
print(fibo(n))