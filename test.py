n,m = map(int,input().split())
arr =[[]*10 for _ in range(10)]
for i in range(0,m):
    a,b = map(int,input().split())
    arr[a].append(b)

for i in range(1,n+1):
    print(i,arr[i])
