s1=input().lower()
s2=input().lower()
a=s1.split()
b=s2.split()
for i in b:
    for j in a:
        if i==j:
            print(i,end=' ')