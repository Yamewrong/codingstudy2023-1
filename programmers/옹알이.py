def solution(babbling):
    answer = 0
    for a in babbling:
        cnt = 0
        if "aya" in a:
            a = a.replace("aya",".")
            cnt = 1
        if "ye" in a :
            a = a.replace("ye",".")
            cnt = 1
        if "woo" in a :
            a = a.replace("woo",".")
            cnt = 1
        if "ma" in a :
            a = a.replace("ma",".")
            cnt = 1
        if cnt == 1:
            a = a.replace(".","")
            if len(a)==0:
                answer = answer+1
    return answer