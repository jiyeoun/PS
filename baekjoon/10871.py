a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(a[0]):
    if b[i] < a[1]:
        print(b[i],end='')
        print(" ",end='')