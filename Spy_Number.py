n=int(input())
sum=0
prod=1
while n>0:
    digit=n%10
    sum=sum+digit
    prod=prod*digit
    n=n//10
if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")
    