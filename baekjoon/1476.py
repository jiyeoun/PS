e,s,m=map(int,input().split())
a=1
b=1
c=1
count=1
while e != a or s != b or m != c :
    if a <= 15:
        a+=1
    if a>15:
        a-=15
    if b<=28:
        b+=1
    if b>28:
        b-=28
    if c <= 19:
        c+=1
    if c>19:
        c-=19
    count+=1

print(count)