n=int(input())
ans=0
while n:
    r=n%10
    ans+=r**2
    n=n//10
    if n==0 and ans<10:
        if ans==1 or ans==7:
            print(True)
            break
        else:
            print(False)
    elif n==0 and ans>9:
        n=ans
        ans=0
        
    