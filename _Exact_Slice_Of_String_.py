string = input()
f = int(input())
s= int(input())
l = len(string)
for i in range(0,l):
    if i>=f and i<=s:
        print(string[i],end="")