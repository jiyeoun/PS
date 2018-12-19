import math

n=int(input())
a=2
for i in range(n-1):
    if n%a==0:
        n=n//a
        print(a)
    else:
        a+=1