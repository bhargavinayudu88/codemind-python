n=int(input())
b=list(map(int,input().split()))
sum=sum(b)
avg=sum//n
if avg in b:
    print(True)
else:
    print(False)

