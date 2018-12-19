a= int(input())
c=''
for i in range(a):
    a,b=input().split()
    a= int(a)
    for j in range(len(b)):
        c+=b[j]*a
    print(c)
    c=''