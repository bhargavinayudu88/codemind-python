n,m=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
c=[]
for i in N:
    if i not in M:
        if i not in c:
            c.append(i)
for i in M:
    if i not in N:
        if i not in c:
            c.append(i)
print(*c)