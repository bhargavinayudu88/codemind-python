n=int(input())
t=n
sum=0
while n!=0:
    r=n%10
    n=n//10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
if sum==t:
    print("The number" ,sum ,"is a strong number")
else:
    print("The number" ,t ,"is not a strong number")
        
        