#def 순회 중에 현재 방문 중인 정점의 번호를 출력하는 함수
n,m = map(int,input().split())
arr = [[]*1000 for _ in range(1001)]
bool =[False]*1001
def dfs(n):
    bool[n]=True
    print(n)
    for next in arr[n]:
        if bool[next]==False:
            dfs(next)
for i in range(0,m):
    a,b= map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,n+1):
    print(i,":",arr[i])
dfs(1)
