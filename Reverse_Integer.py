n= (input())
rev=""
for i in n:
    if i!='-' and i!='0':
        rev=i+rev
    elif i=='-':
        print("-",end="")
print(rev)