n=int(input())
for i in range(n):
    a=int(input())
    for j in range(1,a):
        c=0
        if j**2==a:
            c=c+1
            break
    if c==1:
        print(True)
    else:
        print(False)
        
