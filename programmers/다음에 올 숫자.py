def find(common):
    end = len(common)
    list =[]
    cnt = 0
    for i in range(0,end-1):
        list.append(common[i+1]-common[i])
    for i in range(0,len(list)-1):
        if list[i+1] == list[i]:
            cnt = 1
        else: cnt = 2
    if cnt == 1:
        return 1,common[1]-common[0]
    if cnt == 2:
        return 2,common[1]/common[0]

def solution(common):
    a,b = find(common)
    if a == 1:
        return common[len(common)-1]+b
    if a == 2:
        return common[len(common)-1]*b