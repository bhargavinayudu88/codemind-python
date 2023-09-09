n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i>=0:
        a.append(len(str(i)))
    else:
        i=-i
        a.append(len(str(i)))
        
print(*a)