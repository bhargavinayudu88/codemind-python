n=int(input())
sum=0
sqrt=n*n
while sqrt>0:
    digit=sqrt%10
    sum=sum+digit
    sqrt=sqrt//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")