#def 순회 중에 현재 방문 중인 정점의 번호를 출력하는 함수
#n,m = map(int,input().split())
n = int(input())
m = int(input())
arr = [[]*1000 for _ in range(1001)]
bool =[False]*1001
def dfs(n):
    bool[n]=True
    ret = 1
    for next in arr[n]:
        if bool[next]==False:
            ret = ret + dfs(next)
    return ret
for i in range(0,m):
    a,b= map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
#for i in range(1,n+1):
#    print(i,":",arr[i])
print(dfs(1)-1)
