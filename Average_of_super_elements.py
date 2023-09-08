n=int(input())
l=list(map(int,input().split()))
v=[]
for i in range(len(l)):
    c=1
    if (l[i]==-1):
        continue
    for j in range(len(l)):
        if(i!=j and l[i]==l[j]):
            c+=1
            l[j]=-1
    if(c==l[i]):
        v.append(l[i])
if(len(v)>0):
    s=sum(v)/len(v)
    print("%.2f"%s)
else:
    print("-1")
    