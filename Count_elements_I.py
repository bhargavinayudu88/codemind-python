n,m=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
c=[]
if n>m:

    for i in M:
        if i in N and i not in c:
            c.append(i)
else:
    for i in N:
        if i in M and i not in c:
            c.append(i)
    
    
print(len(c))