a=int(input())
b=int(input())

for i in range(a,b):
    s=0
    c=i
    while c!=0:
        r=c%10
        s=s*10+r
        c=c//10
    if i==s:
        print(s,end=" ")