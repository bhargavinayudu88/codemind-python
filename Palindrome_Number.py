n=int(input())
for i in range(n):
    x=int(input())
    m=x
    s=0
    while x!=0:
        r=x%10
        s=s*10+r
        x=x//10
        if m==s:
            print(True)
            break
    else:
        print(False)