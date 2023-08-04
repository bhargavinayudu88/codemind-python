n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    a=i**0.5
    c=int(a)
    if c==a:
        s=s+i
print(s)