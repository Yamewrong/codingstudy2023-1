def solution(num, total):
    answer = []
    cnt=0
    sum=0
    for i in range(0,num):
        sum=sum+cnt
        cnt=cnt+1
    n=int((total-sum)/num)
    for i in range(0,num):
        answer.append(n+i)
    return answer