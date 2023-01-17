import sys
sys.setrecursionlimit(10**5)
def dfs(x,y):
    #범위
    if y<=-1 or x<=-1 or y>=n or x>=m:
        return False
    #더이상 안나오면 덩어리 하나 끝 !
    if graph[y][x]==1:
        graph[y][x]=0 #한번 방문한 곳은 방문처리
        dfs(x-1,y) # 상
        dfs(x+1,y) # 하
        dfs(x,y-1) # 좌
        dfs(x,y+1) # 우
        return True
    return False

t = int(input())
res=[]
while(t>0):
    m,n,k = map(int,input().split())
    graph=[[]*51 for _ in range(51)]
    for i in range(n):
        for j in range(m):
            graph[i].append(0)    
    for i in range(k):
        b,a = map(int,input().split())
        graph[a][b]=1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                result+=1
    res.append(result)
    t-=1
a=len(res)
for i in range(0,a):
    print(res[i])
#  0 1 2 3 4 5 6 7 8 9
#0 1 1 0 0 0 0 0 0 0 0
#1 0 1 0 0 0 0 0 0 0 0
#2 0 0 0 0 1 0 0 0 0 0
#3 0 0 0 0 1 0 0 0 0 0
#4 0 0 1 1 0 0 0 1 1 1
#5 0 0 0 0 X 0 0 1 1 1
#6 0 0 0 0 0 0 0 1 1 1
#7 0 0 0 0 0 0 0 0 0 0