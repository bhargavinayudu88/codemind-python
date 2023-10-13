n=input()
s=n.split()
v='aeiouAEIOU'
e=[]
count=0
for i in s:
    count=0
    for j in i:
        if j in v:
            count+=1
    e.append(count)
print(min(e))