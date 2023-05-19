n=int(input())
for i in range(n):
    x=int(input())
    if x==0:
        print("1")
    else:
        fact=1
        for j in range(1,x+1):
            fact=fact*j
    print(fact)