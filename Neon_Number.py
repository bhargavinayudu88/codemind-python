n=int(input())
s=0
sq=n**2
while sq>0:
    r=sq%10
    s=s+r
    sq=sq//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")