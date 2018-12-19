a,b=input().split()
a=int(a)
b=int(b)
sum=0
l = []

for i in range(1000):
    for j in range(i):
        l.append(i)

for k in range(a-1,b):
    sum+=l[k]

print(sum)