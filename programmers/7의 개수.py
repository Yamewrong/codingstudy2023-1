def solution(array):
    cnt = 0
    a = len(array)
    arr=''
    for i in range(0,a):
        k=str(array[i])
        arr = arr+k
    for i in range(0,len(arr)):
        if(arr[i]=='7'):
            cnt=cnt+1
    return cnt