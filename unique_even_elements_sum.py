n=int(input())
b=list(map(int,input().split()))
a=[]
for i in b:
    if i%2==0 and i not in a:
        a.append(i)
print(sum(a))