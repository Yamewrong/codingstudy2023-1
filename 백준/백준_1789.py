n = int(input())
a=2
sum=0
while True:
    a = a+1
    sum =a*(a+1)//2
    if n<sum:
        a=a-1
        break

if n <=2 :
    print("1")
else:
    print(a)
