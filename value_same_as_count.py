a=int(input())
s=list(map(int,input().split()))
d=list(set(s))
c=0
for i in d:
    if(i==s.count(i)):
        c+=1
print(c)