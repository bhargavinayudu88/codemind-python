n=input()
s=n.split()
v='aeiouAEIOU'
count=0
for i in s:
    count=0
    for j in i:
        if j in v:
            count+=1
    print(count,end=" ")