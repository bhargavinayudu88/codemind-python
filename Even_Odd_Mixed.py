n=int(input())
even=0
odd=0
while (n):
    r=n%10
    if r%2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10
if even>0 and odd==0:
    print("Even")
elif even==0 and odd>0:
    print("Odd")
else:
    print("Mixed")
    