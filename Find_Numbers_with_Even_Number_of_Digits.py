n=int(input())
a=list(input().split())
count=0
for i in a:
    if len(i)%2==0:
        count=count+1
print(count)

