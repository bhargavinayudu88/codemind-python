n=int(input())
c=0
l=[]
for i in range(1,n+1):
    a=int(input())
    l.append(a)
t=int(input())
for i in l:
    if i<=t:
        c+=1
    else:
        c+=2
print(c)
