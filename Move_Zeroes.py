n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i!=0:
        b.append(i)
for i in range(n-len(b)):
    b.append(0)
for i in b:
    print(i,end=' ')