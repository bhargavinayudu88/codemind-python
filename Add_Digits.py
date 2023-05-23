n=int(input())
def fun(n):
    s=0
    while n:
        r=n%10
        s=s+r
        n=n//10
    return s
while n>10:
    n=fun(n)
print(n)
    